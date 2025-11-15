
# PDU Device API (Local, DB-backed Users + JWT)

FastAPI + SQLAlchemy app connecting to **local MySQL** with:
- `device` table CRUD (protected)
- DB-backed `users` with bcrypt-hashed passwords
- JWT login (`/auth/token`)
- Admin-only user management

## Prerequisites
- Python 3.10+
- MySQL running locally on 127.0.0.1:3306

## 1) Create DB & tables
```bash
mysql -u root -p < mysql/01_device.sql
mysql -u root -p < mysql/02_users.sql
```

## 2) Configure `.env`
Copy the sample and edit values:
```bash
cp app/.env.sample app/.env
# edit app/.env (DB_*, SECRET_KEY, ADMIN_* for seeding)
```
Generate a strong SECRET_KEY:
```bash
python - <<'PY'
import secrets; print(secrets.token_hex(32))
PY
```

## 3) Seed the first admin
```bash
PYTHONPATH=. python scripts/seed_admin.py
```

## 4) Run the API
```bash
./scripts/run_local.sh
# open http://127.0.0.1:8000/docs
```

## 5) Login & use
```bash
curl -X POST http://127.0.0.1:8000/auth/token   -H 'Content-Type: application/x-www-form-urlencoded'   -d 'username=admin&password=<your-admin-pass>'
```
Use the token (Bearer) in Swagger UI (Authorize) or via curl.

## Endpoints
- `POST /auth/token` – login with username/password → JWT
- `GET /devices`, `POST /devices`, `PUT/PATCH/DELETE /devices/{id}` – protected
- `GET /users` – list users (admin only)
- `POST /users` – create user (admin only)
- `GET /users/{id}` – get user (admin only)
- `DELETE /users/{id}` – delete user (admin only)

## Notes
- Switch to Alembic for production migrations.
- Rotate `SECRET_KEY`; never commit real secrets.
- Consider adding scopes/roles to JWT if you need finer control.
