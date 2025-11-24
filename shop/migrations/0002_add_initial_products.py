# Data migration to add initial products

from django.db import migrations
from decimal import Decimal


def add_initial_products(apps, schema_editor):
    """Add 3 initial products to the database."""
    Product = apps.get_model('shop', 'Product')
    
    products = [
        {
            'name': 'Premium Wireless Headphones',
            'description': 'High-quality wireless headphones with active noise cancellation and 30-hour battery life.',
            'price': Decimal('199.99')
        },
        {
            'name': 'Smart Watch Pro',
            'description': 'Advanced fitness tracking, heart rate monitoring, GPS, and water resistance up to 50m.',
            'price': Decimal('349.99')
        },
        {
            'name': 'Portable Power Bank',
            'description': '20,000mAh high-capacity power bank with fast charging and dual USB ports.',
            'price': Decimal('49.99')
        },
    ]
    
    for product_data in products:
        Product.objects.create(**product_data)


def remove_initial_products(apps, schema_editor):
    """Remove the initial products (reverse migration)."""
    Product = apps.get_model('shop', 'Product')
    Product.objects.filter(
        name__in=[
            'Premium Wireless Headphones',
            'Smart Watch Pro',
            'Portable Power Bank'
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_products, remove_initial_products),
    ]


