# Django + PostgreSQL + Stripe E-commerce Project

A fully functional e-commerce application with Django, PostgreSQL (Render cloud), and Stripe payment integration.

## 🚀 Quick Start (After Cloning)

### ⚠️ IMPORTANT: First-Time Setup

After cloning this repository, you **MUST** create a `.env` file:

```bash
# 1. Copy the environment template file
cp env_template.txt .env

# 2. The .env file already has the database credentials
#    You only need to add your Stripe keys:
#    - Edit .env
#    - Replace STRIPE_PUBLIC_KEY with your key from https://dashboard.stripe.com/test/apikeys
#    - Replace STRIPE_SECRET_KEY with your key
```

### Running the Project

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin user
python create_admin.py

# 6. Start server
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

---

## 🔑 Getting Stripe Keys

1. Go to: https://dashboard.stripe.com/register
2. Sign up (free)
3. Switch to **Test Mode** (toggle top-right)
4. Go to: **Developers** → **API keys**
5. Copy:
   - **Publishable key** (pk_test_...)
   - **Secret key** (sk_test_...)
6. Add them to `.env` file

---

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
├── env_template.txt      # Environment template
└── README.md             # This file
```

---

## 🛠️ Common Commands

```bash
# Start server
python run.py

# Create admin user
python create_admin.py

# Run migrations
python manage.py migrate

# Django shell
python manage.py shell

# Access admin panel
# http://localhost:8000/admin
```

---

## 🐳 Docker (Alternative)

```bash
# Create .env file first!
cp env_template.txt .env

# Start with Docker
docker-compose up

# Run migrations
docker-compose exec web python manage.py migrate

# Create admin
docker-compose exec web python manage.py createsuperuser
```

---

## ❓ Troubleshooting

### "Connection to server at localhost failed"

**Problem**: `.env` file is missing

**Solution**:
```bash
cp env_template.txt .env
# Database credentials are already in the file
# Just add your Stripe keys
```

### "Stripe authentication failed"

**Problem**: Stripe keys not configured

**Solution**:
1. Get keys from https://dashboard.stripe.com/test/apikeys
2. Update `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` in `.env`
3. Restart server

### "No module named django"

**Problem**: Virtual environment not activated or dependencies not installed

**Solution**:
```bash
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

---

## 🔐 Security

- ✅ `.env` file is in `.gitignore` (never commit it!)
- ✅ Use test mode Stripe keys for development
- ✅ Cloud database credentials included in `env_template.txt`
- ✅ Unique session IDs prevent double payments

---

## 📊 Database

**Provider**: Render (Cloud PostgreSQL)
**Location**: Singapore
**Connection**: Configured in `.env.example`

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

---

## 📞 Support

For issues:
1. Check `.env` file exists and has correct values
2. Verify virtual environment is activated
3. Ensure all dependencies are installed
4. Check Django logs for detailed errors

---

## 🚀 Tech Stack

- **Backend**: Django 5.0
- **Database**: PostgreSQL (Render Cloud)
- **Payment**: Stripe (Test Mode)
- **Frontend**: Bootstrap 5
- **Deployment**: Docker-ready

---

**Built with ❤️ for the assignment**

