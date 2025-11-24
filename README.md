# Django + PostgreSQL + Stripe E-commerce Project

A fully functional e-commerce application with Django, PostgreSQL (Render cloud), and Stripe payment integration.

clone the repo- https://github.com/Shivani-Chauhan-Dev/stripe_e_commerce_project.git

## 🚀 Quick Start (After Cloning)

### ⚠️ IMPORTANT: First-Time Setup (DO THIS FIRST!)

**🚨 CRITICAL: After cloning, you MUST create `.env` file or the app won't work!**

Without `.env` file, you'll get **403 Forbidden** errors when clicking "Buy Now".

**Step 1: Create `.env` file from the example**

```bash
# Copy the example file
cp env.example .env      # Linux/macOS
copy env.example .env    # Windows

# Or manually create .env file
notepad .env             # Windows
nano .env                # Linux/macOS
code .env                # VS Code
```

**Step 2: Fill in the actual values**

Open `.env` file and replace the placeholder values with:
- **Database credentials** (get from team lead or Render dashboard)
- **Stripe API keys** (get from https://dashboard.stripe.com/test/apikeys)
- **Django SECRET_KEY** (generate a new one or get from team lead)

### Running the Project

```bash
# 1. Create .env file (paste content from team lead)
# See above ☝️

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python create_admin.py

# 7. Start server
python run.py
```

Visit: **http://localhost:8000**

---

## ✨ Features

- 🛍️ Product catalog with 3 pre-loaded products
- 💳 Stripe Checkout integration (test mode)
- 📦 Order management system
- 🔒 Double payment prevention
- 🎨 Modern Bootstrap UI
- ☁️ Cloud PostgreSQL (Render)
- 🐳 Docker support


## 💳 Test Payment

Use test card: **4242 4242 4242 4242**
- Expiry: Any future date
- CVC: Any 3 digits
- ZIP: Any 5 digits

---

## 📁 Project Structure

```
stripe_e_commerce_project/
├── shop/                   # Main app
│   ├── models.py          # Product, Order, OrderItem
│   ├── views.py           # Checkout & payment logic
│   ├── templates/         # HTML templates
│   └── migrations/        # Database migrations
├── stripe_shop/           # Django project settings
├── manage.py              # Django management
├── run.py                 # Start server script
├── create_admin.py        # Create admin user script
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
├── .env                  # Your actual config (create from env.example)
└── README.md             # This file


## 🐳 Docker (Alternative)

```bash
# Create .env file first
cp env.example .env
# Edit .env with database credentials and Stripe keys

# Start with Docker
docker-compose up

# Run migrations
docker-compose exec web python manage.py migrate

# Create admin
docker-compose exec web python manage.py createsuperuser


## 📊 Database

**Provider**: Render (Cloud PostgreSQL)
**Location**: Singapore

---

## 🎯 Assignment Checklist

- ✅ Django 5.0 (latest)
- ✅ PostgreSQL database
- ✅ Stripe test mode integration
- ✅ 3 products displayed
- ✅ Stripe Checkout Session
- ✅ Order creation on success
- ✅ "My Orders" display
- ✅ Double payment prevention
- ✅ Bootstrap UI
- ✅ Docker support
- ✅ Platform-independent



## 🔑 How to Get Required Keys

### Stripe API Keys

1. Go to: https://dashboard.stripe.com/register
2. Sign up (free account)
3. Switch to **Test Mode** (toggle in top-right)
4. Go to: **Developers** → **API keys**
5. Copy:
   - **Publishable key** (starts with `pk_test_...`)
   - **Secret key** (starts with `sk_test_...`)
6. Paste them into `.env` file

### Django SECRET_KEY

Generate a secure random key:

```python
# Option 1: Using Django
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Option 2: Using Python
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Copy the output and paste it into `.env` as `SECRET_KEY`

### Database Credentials

Get these from:
- **Your team lead** (if joining existing project)
- **Render dashboard** (if you created the database)

---

## 🚀 Tech Stack

- **Backend**: Django 5.0
- **Database**: PostgreSQL (Render Cloud)
- **Payment**: Stripe (Test Mode)
- **Frontend**: Bootstrap 5
- **Deployment**: Docker-ready

---

**Built with ❤️ for the assignment**

