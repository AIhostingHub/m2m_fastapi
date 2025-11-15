
from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import devices
from app.auth import auth_router
from app.routers import users as users_router

# Auto-create tables (for dev). Use Alembic in production.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PDU Device API (Local, DB-auth)", version="1.4.0")

# Routers
app.include_router(auth_router)
app.include_router(users_router.router)
app.include_router(devices.router)

@app.get("/health")
def health():
    return {"status": "ok"}
