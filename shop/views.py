

from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.db import transaction
import stripe
import json

from .models import Product, Order, OrderItem

# Configure Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    """Display products and order list."""
    products = Product.objects.all()
    orders = Order.objects.filter(status='paid').prefetch_related('items__product')
    
    context = {
        'products': products,
        'orders': orders,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'shop/index.html', context)


@require_http_methods(["POST"])
def create_checkout_session(request):
    """Create a Stripe Checkout Session for the selected products."""
    try:
        # Parse the cart data from the request
        cart_data = json.loads(request.body)
        
        if not cart_data:
            return JsonResponse({'error': 'Cart is empty'}, status=400)
        
        # Build line items for Stripe
        line_items = []
        total_amount = 0
        
        for item in cart_data:
            product_id = item.get('product_id')
            quantity = item.get('quantity', 1)
            
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse(
                    {'error': f'Product {product_id} not found'},
                    status=404
                )
            
            if quantity < 1:
                return JsonResponse(
                    {'error': 'Quantity must be at least 1'},
                    status=400
                )
            
            # Calculate total
            total_amount += float(product.price) * quantity
            
            # Add to Stripe line items
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product.price * 100),  # Convert to cents
                    'product_data': {
                        'name': product.name,
                        'description': product.description,
                    },
                },
                'quantity': quantity,
            })
        
        # Create Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=settings.DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.DOMAIN + '/',
            metadata={
                'cart_data': json.dumps(cart_data),
            }
        )
        
        return JsonResponse({'id': checkout_session.id})
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def success(request):
    """Handle successful payment and create order."""
    session_id = request.GET.get('session_id')
    
    if not session_id:
        return redirect('index')
    
    try:
        # Check if order already exists (prevent double payment)
        if Order.objects.filter(stripe_session_id=session_id).exists():
            # Order already processed, just redirect to index
            return redirect('index')
        
        # Retrieve the session from Stripe
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        
        # Verify payment status
        if checkout_session.payment_status != 'paid':
            return redirect('index')
        
        # Get cart data from metadata
        metadata = checkout_session.metadata or {}
        cart_data = json.loads(metadata.get('cart_data', '[]'))
        
        if not cart_data:
            return redirect('index')
        
        # Create order with transaction to ensure atomicity
        with transaction.atomic():  # type: ignore[attr-defined]
            # Calculate total amount
            total_amount = 0
            order_items_data = []
            
            for item in cart_data:
                product = Product.objects.get(id=item['product_id'])
                quantity = item['quantity']
                price = product.price
                
                total_amount += float(price) * quantity
                order_items_data.append({
                    'product': product,
                    'quantity': quantity,
                    'price': price,
                })
            
            # Create the order
            order = Order.objects.create(
                stripe_session_id=session_id,
                status='paid',
                total_amount=total_amount
            )
            
            # Create order items
            for item_data in order_items_data:
                OrderItem.objects.create(
                    order=order,
                    product=item_data['product'],
                    quantity=item_data['quantity'],
                    price=item_data['price']
                )
        
        return redirect('index')
    
    except stripe.error.StripeError as e:  # type: ignore[attr-defined]
        print(f"Stripe error: {str(e)}")
        return redirect('index')
    except Exception as e:
        print(f"Error processing order: {str(e)}")
        return redirect('index')


@csrf_exempt
@require_http_methods(["POST"])
def stripe_webhook(request):
    """Handle Stripe webhooks for additional payment verification."""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:  # type: ignore[attr-defined]
        # Invalid signature
        return HttpResponse(status=400)
    
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session['id']
        
        # Check if order already exists
        if not Order.objects.filter(stripe_session_id=session_id).exists():
            # Process the order (same logic as success view)
            # This is a backup in case the success redirect fails
            pass
    
    return HttpResponse(status=200)
