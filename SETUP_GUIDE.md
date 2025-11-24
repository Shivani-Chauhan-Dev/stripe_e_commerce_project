# 🚀 Setup Guide - After Cloning

## For Team Members

If you just cloned this repo, follow these steps:

### Step 1: Get `.env` File Content

Ask your team lead for the `.env` file content via:
- 💬 Slack/Teams
- 📧 Email
- 🔒 Secure password manager

The `.env` file contains configuration like database credentials and Stripe API keys.

### Step 2: Create `.env` File

**Windows (PowerShell/CMD):**
```bash
notepad .env
```
- Paste the content you received
- Press `Ctrl+S` to save
- Close Notepad

**Linux/macOS:**
```bash
nano .env
```
- Paste the content you received
- Press `Ctrl+X`, then `Y`, then `Enter`

**Or use your favorite editor:**
```bash
code .env    # VS Code
vim .env     # Vim
subl .env    # Sublime Text
```

### Step 3: Setup Environment

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

### Step 4: Test It

Visit: http://localhost:8000

Click "Buy Now" - if it redirects to Stripe, you're all set! ✅

---

## For Team Leads

When a new team member joins:

1. **Copy your `.env` file content**
2. **Send to them securely via:**
   - 💬 Slack/Teams DM
   - 🔐 Password manager (1Password, LastPass, Bitwarden)
   - 📧 Encrypted email
3. **Tell them to:**
   - Create `.env` file in project root
   - Paste the content
   - Run setup commands

---

## Why This Approach?

✅ **Simple**: Just copy-paste and run  
✅ **Secure**: `.env` never committed to Git  
✅ **Fast**: No interactive scripts needed  
✅ **Platform-independent**: Works on Windows/Linux/macOS  
✅ **Team-friendly**: Easy to share via existing communication tools  

---

## Troubleshooting

**Q: I created `.env` but still get 403 errors**  
A: Restart the Django server after creating `.env`

**Q: How do I verify my `.env` file is correct?**  
A: Check it exists: `dir .env` (Windows) or `ls -la .env` (Linux/macOS)

**Q: Can I share `.env` file via Git?**  
A: ❌ **NO!** Never commit `.env` - it contains secrets!

**Q: Where do I get Stripe keys?**  
A: https://dashboard.stripe.com/test/apikeys (test mode)

---

## Security Reminder

🔒 **NEVER commit `.env` to Git!**

It's already in `.gitignore`, but always double-check:

```bash
git status  # Should NOT show .env file
```

If you accidentally committed it:
1. Remove it immediately
2. Rotate all credentials (database password, Stripe keys)
3. Update `.gitignore`

---

**Need help?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

