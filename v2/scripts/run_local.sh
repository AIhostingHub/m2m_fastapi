
#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
if [ ! -f app/.env ]; then
  echo "Copying app/.env.sample to app/.env (edit values!)"
  cp app/.env.sample app/.env
fi
uvicorn app.main:app --host $(grep ^UVICORN_HOST app/.env | cut -d= -f2 | tr -d '') --port $(grep ^UVICORN_PORT app/.env | cut -d= -f2 | tr -d '')
