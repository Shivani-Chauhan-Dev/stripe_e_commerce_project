# Django + PostgreSQL + Stripe E-commerce Project

A fully functional e-commerce application with Django, PostgreSQL (Render cloud), and Stripe payment integration.

## 🚀 Quick Start (After Cloning)

### ⚠️ IMPORTANT: First-Time Setup (DO THIS FIRST!)

**🚨 CRITICAL: After cloning, you MUST configure `.env` file or the app won't work!**

Without `.env` file, you'll get **403 Forbidden** errors when clicking "Buy Now".

**Option 1: Interactive Setup (Recommended)**
```bash
python setup_project.py
```

This will:
1. ✅ Create `.env` file automatically
2. ✅ Ask for database credentials
3. ✅ Ask for Stripe API keys
4. ✅ Guide you through setup

**Option 2: Manual Setup**
```bash
# Copy template
cp env.example .env    # Linux/macOS
copy env.example .env  # Windows

# Edit .env file and add:
# - Database credentials (from team lead)
# - Stripe keys (from https://dashboard.stripe.com/test/apikeys)
```

**Why this is required:**
- `.env` file is NOT in Git (for security)
- Contains database credentials and Stripe keys
- App will fail without it (403 errors on checkout)

### Running the Project

```bash
# 1. Run setup script (creates .env with your credentials)
python setup_project.py

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

## 🚨 Troubleshooting "Buy Now" Button Issues

**Error: 403 Forbidden or "Unexpected token '<'..."**

**Cause**: `.env` file is missing or Stripe keys not configured

**Fix**:
1. Verify `.env` file exists in project root
2. Check `.env` has your Stripe keys
3. Restart server after editing `.env`

**See [AFTER_CLONE_README.md](AFTER_CLONE_README.md) for detailed first-time setup!**

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
├── setup_project.py      # Setup script (run after cloning)
├── env.example           # Environment template (in Git)
├── .env                  # Your config (created by setup_project.py)
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
# Create .env file first
cp env.example .env
# Edit .env with database credentials and Stripe keys

# Start with Docker
docker-compose up

# Run migrations
docker-compose exec web python manage.py migrate

# Create admin
docker-compose exec web python manage.py createsuperuser
```

---

## ❓ Troubleshooting

### "Connection to server at localhost failed" / "password authentication failed for user postgres"

**Problem**: `.env` file is missing (common after cloning)

**Solution:**

**Option 1: Use Setup Script (Easiest)**
```bash
python setup_project.py
# Follow the interactive prompts
```

**Option 2: Manual Setup**
1. Copy: `cp env.example .env`
2. Get database credentials from team lead
3. Edit `.env` with credentials and Stripe keys

**Why this happens:**
- `.env` file is NOT in Git (for security)
- After cloning, the `.env` file doesn't exist
- Without `.env`, Django tries to connect to `localhost`
- You need actual database credentials from your team to connect!

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
- ✅ Database credentials shared securely (not in Git)
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

