# Django + PostgreSQL + Stripe E-commerce Project

A fully functional e-commerce application with Django, PostgreSQL (Render cloud), and Stripe payment integration.

clone the repo- https://github.com/Shivani-Chauhan-Dev/stripe_e_commerce_project.git

## 🚀 Quick Start (After Cloning)

### ⚠️ IMPORTANT: First-Time Setup (DO THIS FIRST!)

**🚨 CRITICAL: After cloning, you MUST create `.env` file or the app won't work!**

Without `.env` file, you'll get **403 Forbidden** errors when clicking "Buy Now".

**Step 1: Get the `.env` file content from your team lead** (via Slack/Email)

**Step 2: Create `.env` file and paste the content**

```bash
# Windows (PowerShell/CMD)
notepad .env
# Paste the content, save and close

# Linux/macOS
nano .env
# Paste the content, press Ctrl+X, Y, Enter

# Or use any text editor
code .env    # VS Code
vim .env     # Vim
```

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
├── setup_project.py      # Setup script (run after cloning)
├── env.example           # Environment template (in Git)
├── .env                  # Your config (created by setup_project.py)
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



## 🚀 Tech Stack

- **Backend**: Django 5.0
- **Database**: PostgreSQL (Render Cloud)
- **Payment**: Stripe (Test Mode)
- **Frontend**: Bootstrap 5
- **Deployment**: Docker-ready

---

**Built with ❤️ for the assignment**

