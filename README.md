# PropertyOps AI

PropertyOps takes care of a small sales handoff. When a new property enquiry is recorded, n8n creates a follow-up task with the lead already attached.

## How the handoff works

1. FastAPI validates the enquiry and saves it in PostgreSQL.
2. Once the lead is saved, FastAPI sends a `lead.created` event to n8n in the background.
3. n8n calls the follow-up API with the lead ID and a task title. You can see the new task in `GET /follow-up-tasks`.

The API also lets you view leads, update lead status, and mark tasks as they progress. Webhook delivery errors appear in the FastAPI logs.

## Run it locally

You'll need Python, PostgreSQL, and Node.js for n8n. From the repository root in PowerShell, create a virtual environment and install the dependencies.

```powershell
python -m venv .propertyvenv
.\.propertyvenv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a local PostgreSQL database and put its name, user, and password in `.env`.

```dotenv
DB_NAME=propertyops_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

Set `DB_HOST` or `DB_PORT` if you use a host or port other than `localhost:5432`. Apply the migrations and start the API.

```powershell
python -m alembic upgrade head
python -m uvicorn app.main:app --reload
```

## Try the automation

1. In another terminal, run `npx.cmd n8n` and open [n8n](http://localhost:5678).
2. Import [the lead workflow](n8n_workflows/Property_Operation_Workflow.json) and publish or activate it. Its HTTP Request node points at FastAPI on `127.0.0.1:8000`. Update that URL if n8n runs in a separate environment.
3. Copy the Webhook node's production URL into `N8N_WEBHOOK_URL` in `.env`, then restart FastAPI.
4. Open the [API docs](http://127.0.0.1:8000/docs). Submit a test enquiry through `POST /leads/` and check `GET /follow-up-tasks` for a task with the same lead ID.

The repository contains the lead and task APIs, database migrations, and the n8n workflow. A reporting dashboard and document search are planned.
