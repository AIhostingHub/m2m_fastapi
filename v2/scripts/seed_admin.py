
#!/usr/bin/env python3
import os, sys
from dotenv import load_dotenv
from sqlalchemy.orm import Session

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.database import SessionLocal
from app.models import User
from app.auth import pwd_context

if __name__ == "__main__":
    # Load .env next to app package
    load_dotenv(os.path.join(PROJECT_ROOT, 'app', '.env'))
    username = os.getenv('ADMIN_USERNAME')
    password = os.getenv('ADMIN_PASSWORD')
    email = os.getenv('ADMIN_EMAIL')
    if not username or not password:
        print("ADMIN_USERNAME / ADMIN_PASSWORD missing in app/.env")
        sys.exit(1)

    db: Session = SessionLocal()
    try:
        if db.query(User).filter(User.username == username).first():
            print(f"Admin '{username}' already exists.")
            sys.exit(0)
        hashed = pwd_context.hash(password)
        admin = User(username=username, email=email, hashed_password=hashed, is_active=1, is_admin=1)
        db.add(admin)
        db.commit()
        print(f"Admin user '{username}' created.")
    finally:
        db.close()
