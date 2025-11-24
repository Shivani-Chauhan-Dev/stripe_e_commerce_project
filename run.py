#!/usr/bin/env python
"""
Platform-independent script to run Django development server
Works on Windows, Linux, and macOS
"""

import os
import sys
import subprocess
import platform

def main():
    """Run the Django development server."""
    
    print("=" * 50)
    print("Django + Stripe Shop - Starting Server")
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
    
    print()
    print("Starting Django development server...")
    print()
    print("📍 Server: http://localhost:8000")
    print("🔧 Admin: http://localhost:8000/admin")
    print("💳 Test card: 4242 4242 4242 4242")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    print()
    
    # Run Django server
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'runserver'])
    except ImportError as exc:
        print("❌ Error: Django is not installed")
        print()
        print("To install dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print("Server stopped.")
        sys.exit(0)

if __name__ == '__main__':
    main()

