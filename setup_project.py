#!/usr/bin/env python3
"""
Project Setup Script
Run this after cloning the repository to configure your environment
"""

import os
import sys

def create_env_file():
    """Create .env file with user-provided credentials"""
    
    print("=" * 70)
    print("Django + Stripe E-commerce - Project Setup")
    print("=" * 70)
    print()
    
    # Check if .env already exists
    if os.path.exists('.env'):
        print("⚠️  .env file already exists!")
        response = input("Do you want to recreate it? (y/n): ").lower()
        if response != 'y':
            print("Setup cancelled. Existing .env file is unchanged.")
            return False
        print()
    
    print("This script will help you create the .env configuration file.")
    print()
    print("You'll need:")
    print("1. Database credentials (from your team lead)")
    print("2. Stripe API keys (from https://dashboard.stripe.com/test/apikeys)")
    print()
    
    input("Press Enter to continue...")
    print()
    
    # Collect database credentials
    print("-" * 70)
    print("DATABASE CONFIGURATION")
    print("-" * 70)
    print()
    print("Get these credentials from your team lead:")
    print()
    
    db_name = input("Database Name [vipratechdb]: ").strip() or "vipratechdb"
    db_user = input("Database User [vipratechdb_user]: ").strip() or "vipratechdb_user"
    db_password = input("Database Password: ").strip()
    if not db_password:
        print("⚠️  Warning: Password is empty!")
    db_host = input("Database Host [dpg-d4i003n5r7bs73c4vj9g-a.singapore-postgres.render.com]: ").strip() or "dpg-d4i003n5r7bs73c4vj9g-a.singapore-postgres.render.com"
    db_port = input("Database Port [5432]: ").strip() or "5432"
    
    print()
    
    # Collect Stripe credentials
    print("-" * 70)
    print("STRIPE CONFIGURATION")
    print("-" * 70)
    print()
    print("Get your Stripe test keys from:")
    print("https://dashboard.stripe.com/test/apikeys")
    print()
    print("Make sure you're in TEST MODE (toggle at top-right)")
    print()
    
    stripe_public = input("Stripe Publishable Key (pk_test_...): ").strip()
    stripe_secret = input("Stripe Secret Key (sk_test_...): ").strip()
    stripe_webhook = input("Stripe Webhook Secret (optional, press Enter to skip): ").strip() or "whsec_optional"
    
    print()
    
    # Create .env file content
    env_content = f"""# Django Settings
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL Database
DB_NAME={db_name}
DB_USER={db_user}
DB_PASSWORD={db_password}
DB_HOST={db_host}
DB_PORT={db_port}

# Stripe Test Mode Keys
STRIPE_PUBLIC_KEY={stripe_public}
STRIPE_SECRET_KEY={stripe_secret}
STRIPE_WEBHOOK_SECRET={stripe_webhook}

# Application Domain
DOMAIN=http://localhost:8000
"""
    
    # Write .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("=" * 70)
        print("✅ SUCCESS! .env file created")
        print("=" * 70)
        print()
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def show_next_steps():
    """Display next steps for the user"""
    print()
    print("📋 Next Steps:")
    print()
    print("1. Create virtual environment:")
    print("   python -m venv venv")
    print()
    print("2. Activate virtual environment:")
    print("   Linux/macOS: source venv/bin/activate")
    print("   Windows:     venv\\Scripts\\activate")
    print()
    print("3. Install dependencies:")
    print("   pip install -r requirements.txt")
    print()
    print("4. Run database migrations:")
    print("   python manage.py migrate")
    print()
    print("5. Create admin user:")
    print("   python create_admin.py")
    print()
    print("6. Start the server:")
    print("   python run.py")
    print()
    print("7. Open browser:")
    print("   http://localhost:8000")
    print()
    print("=" * 70)
    print("🎉 Setup complete! Follow the steps above to start development.")
    print("=" * 70)

def main():
    """Main setup function"""
    try:
        success = create_env_file()
        if success:
            show_next_steps()
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

