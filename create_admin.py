#!/usr/bin/env python
"""
Platform-independent script to create Django superuser
Works on Windows, Linux, and macOS
"""

import os
import sys
import platform

def main():
    """Create a Django superuser."""
    
    print("=" * 50)
    print("Create Django Admin User")
    print("=" * 50)
    print()
    
    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if not in_venv:
        print("⚠️  Warning: Not running in virtual environment")
        print()
        print("To activate virtual environment:")
        if platform.system() == "Windows":
            print("  .\\venv\\Scripts\\Activate.ps1")
        else:
            print("  source venv/bin/activate")
        print()
        
        response = input("Continue anyway? (y/n): ").lower()
        if response != 'y':
            print("Exiting...")
            return
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stripe_shop.settings')
    
    print("Creating superuser...")
    print("Please enter the following information:")
    print()
    
    # Run Django createsuperuser command
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'createsuperuser'])
        
        print()
        print("=" * 50)
        print("✅ Admin user created successfully!")
        print("=" * 50)
        print()
        print("You can now login at: http://localhost:8000/admin")
        print()
        
    except ImportError as exc:
        print("❌ Error: Django is not installed")
        print()
        print("To install dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print("Cancelled.")
        sys.exit(0)

if __name__ == '__main__':
    main()

