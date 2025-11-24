# Troubleshooting Guide

Common issues and their solutions.

## Database Issues

### Connection Failed to Localhost

**Problem**: `connection to server at "localhost" failed`

**Cause**: Missing or incorrect `.env` file

**Solution**:
```bash
python setup_project.py
# Or manually:
cp env.example .env
# Edit .env with correct credentials
```

### Password Authentication Failed

**Problem**: `password authentication failed for user`

**Cause**: Wrong database password in `.env`

**Solution**:
1. Check `.env` file has correct password
2. Verify credentials with team lead
3. Ensure no extra spaces in `.env`

### Database Does Not Exist

**Problem**: `database "xxx" does not exist`

**Cause**: Database not created on server

**Solution**:
- Contact team lead to create database
- Or create your own database on Render
- Update `.env` with correct database name

## Stripe Issues

### Stripe Authentication Failed

**Problem**: `Invalid API Key provided`

**Cause**: Wrong Stripe keys in `.env`

**Solution**:
1. Go to https://dashboard.stripe.com/test/apikeys
2. Ensure you're in **Test Mode**
3. Copy both keys:
   - Publishable key (pk_test_...)
   - Secret key (sk_test_...)
4. Update `.env` file
5. Restart server

### Payment Not Processing

**Problem**: Checkout button does nothing

**Cause**: JavaScript error or missing Stripe key

**Solution**:
1. Open browser console (F12)
2. Check for JavaScript errors
3. Verify `STRIPE_PUBLIC_KEY` in `.env`
4. Clear browser cache
5. Restart server

### Order Not Created After Payment

**Problem**: Payment succeeds but no order

**Cause**: Error in success handler

**Solution**:
1. Check Django logs for errors
2. Verify database connection
3. Check `stripe_session_id` uniqueness
4. Ensure migrations are applied

## Python/Django Issues

### Python Not Found

**Problem**: `python: command not found`

**Cause**: Python not installed or not in PATH

**Solution**:
```bash
# Check Python installation
python --version
python3 --version

# Add Python to PATH
# Or use full path: /usr/bin/python3
```

### Module Not Found

**Problem**: `ModuleNotFoundError: No module named 'django'`

**Cause**: Virtual environment not activated or packages not installed

**Solution**:
```bash
# Activate venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install packages
pip install -r requirements.txt
```

### Permission Denied on Virtual Environment

**Problem**: Cannot activate virtual environment

**Solution Windows**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Solution Linux/macOS**:
```bash
chmod +x venv/bin/activate
```

## Migration Issues

### Migrations Not Applied

**Problem**: `no such table` errors

**Cause**: Migrations not run

**Solution**:
```bash
python manage.py migrate
```

### Migration Conflicts

**Problem**: `Conflicting migrations detected`

**Cause**: Multiple migration files for same app

**Solution**:
```bash
# Reset migrations (CAREFUL - loses data!)
python manage.py migrate shop zero
python manage.py migrate
```

## Static Files Issues

### CSS/JS Not Loading

**Problem**: Styles not applied

**Cause**: Static files not served properly

**Solution**:
```bash
# Development - Django serves static files
DEBUG=True in .env

# Production
python manage.py collectstatic
```

## Server Issues

### Port Already in Use

**Problem**: `Address already in use`

**Cause**: Another process using port 8000

**Solution**:
```bash
# Find process
lsof -i :8000  # Linux/macOS
netstat -ano | findstr :8000  # Windows

# Kill process or use different port
python manage.py runserver 8080
```

### Server Won't Start

**Problem**: Server crashes on start

**Cause**: Various (check error message)

**Solution**:
```bash
# Check for issues
python manage.py check

# Check deployment settings
python manage.py check --deploy

# View detailed errors
python manage.py runserver --traceback
```

## Docker Issues

### Docker Build Fails

**Problem**: Build errors

**Cause**: Missing files or wrong configuration

**Solution**:
```bash
# Rebuild from scratch
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### Database Connection in Docker

**Problem**: Cannot connect to database from container

**Cause**: Wrong DB_HOST in `.env`

**Solution**:
```env
# For Docker Compose, use service name
DB_HOST=db

# For local development
DB_HOST=localhost
```

## Browser Issues

### CSRF Verification Failed

**Problem**: `CSRF verification failed`

**Cause**: CSRF token missing or invalid

**Solution**:
1. Hard refresh browser (Ctrl+Shift+R)
2. Clear cookies
3. Check `{% csrf_token %}` in template
4. Verify CSRF middleware is enabled

### Session Errors

**Problem**: Cart not persisting

**Cause**: Session issues

**Solution**:
```bash
# Clear sessions
python manage.py clearsessions

# Check session configuration
# In Django settings
```

## Environment Issues

### .env File Not Loaded

**Problem**: Settings not reading from `.env`

**Cause**: Missing python-decouple or wrong import

**Solution**:
```bash
pip install python-decouple

# In settings.py
from decouple import config
```

### Wrong Python Version

**Problem**: Using Python 2 instead of 3

**Cause**: System default is Python 2

**Solution**:
```bash
# Use python3 explicitly
python3 -m venv venv
python3 manage.py runserver
```

## Common Error Messages

### "Table already exists"

**Solution**: Migration file needs to be updated or deleted

### "No changes detected"

**Solution**: 
```bash
python manage.py makemigrations --empty app_name
```

### "Broken pipe" or "Connection reset"

**Solution**: Restart development server

### "Invalid syntax"

**Solution**: Check Python version compatibility

## Still Having Issues?

1. Check Django logs
2. Review error message carefully
3. Search error message online
4. Check Django documentation
5. Ask team lead
6. Review README.md
7. Check COMMANDS.md for correct syntax

## Debugging Tips

```bash
# Enable Django debug toolbar
pip install django-debug-toolbar

# Run with verbose output
python manage.py runserver --verbosity 3

# Check Python environment
python -c "import sys; print(sys.executable)"

# Check Django version
python -m django --version

# List installed packages
pip list

# Check for outdated packages
pip list --outdated
```

## Log Files

Check these locations for logs:
- Django console output
- Browser console (F12)
- System logs (`/var/log/`)
- Docker logs (`docker-compose logs`)

## Getting Help

When asking for help, provide:
1. Error message (full text)
2. What you were trying to do
3. What you've already tried
4. Your environment (OS, Python version)
5. Relevant code or configuration

