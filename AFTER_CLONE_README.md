# ⚠️ AFTER CLONING - READ THIS FIRST!

## Why Am I Seeing This?

If you just cloned this repository and tried to run it, you probably got errors like:

- ❌ **403 Forbidden** when clicking "Buy Now"
- ❌ **Connection to localhost failed**
- ❌ **Stripe authentication error**

## Why It Doesn't Work Immediately

The `.env` configuration file is **NOT in Git** (for security). Without it:

- No database connection
- No Stripe keys
- App fails with errors

## Fix It in 2 Minutes

### Step 1: Create `.env` File

**Get the `.env` file content from your team lead** (via Slack/Email/Teams)

Then create the file:

```bash
# Windows
notepad .env
# Paste the content, save and close

# Linux/macOS
nano .env
# Paste the content, press Ctrl+X, Y, Enter
```

### Step 2: Continue Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python create_admin.py

# Start server
python run.py
```

### Step 3: Test It

Visit: http://localhost:8000

Now "Buy Now" button will work! ✅

## Common Mistake

❌ **DON'T DO THIS:**
```bash
git clone <repo>
cd project
python run.py  # ← This will FAIL!
```

✅ **DO THIS:**
```bash
git clone <repo>
cd project
# Create .env file and paste content from team lead
notepad .env  # Windows
nano .env     # Linux/macOS
# Paste, save, then continue
python manage.py migrate
python run.py  # ← Now it works!
```

## Why Your Local Version Works

Your local version works because you already have:
- `.env` file with credentials
- Virtual environment set up
- Database migrated

After cloning, a fresh copy has NONE of these!

## Quick Checklist

After cloning, you need:
- [ ] `.env` file created and pasted (get content from team lead)
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Migrations run
- [ ] Admin user created

## Still Having Issues?

1. Check `.env` file exists: `ls -la .env` (Linux/macOS) or `dir .env` (Windows)
2. Verify `.env` file has content (not empty)
3. Verify Stripe keys in `.env` start with `pk_test_` and `sk_test_`
4. Check database credentials are correct
5. Restart the server after creating `.env`
6. See TROUBLESHOOTING.md for more help

## Summary

**The golden rule after cloning:**

1. **Get `.env` content from team lead** (Slack/Email)
2. **Create `.env` file and paste it**
3. **Run migrations and start server**

That's it! Simple and secure! 🎉

