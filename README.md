# PropertyOps AI

PropertyOps AI is a property sales and operations automation system. It manages customer leads, creates follow-up tasks, automates workflows with n8n, and displays operational data through a Streamlit dashboard.

## Current Features

* Create and view customer leads
* Update lead status
* Create and manage follow-up tasks
* Store data in PostgreSQL
* Manage database changes with Alembic
* Automatically create follow-up tasks using n8n
* View lead and task metrics in a Streamlit dashboard

## In Progress

* Document-based RAG assistant
* Local Hugging Face embeddings
* ChromaDB document search
* Marketing and financial analysis

## Technology Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* n8n
* Streamlit
* LangChain
* ChromaDB
* Hugging Face

## Project Structure

```text
propertyoperation_ai/
├── alembic/
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── config.py
│   ├── database.py
│   └── main.py
├── dashboard/
├── n8n_workflows/
├── policy_documents/
├── .env.example
├── alembic.ini
├── requirements.txt
└── README.md
```

## Local Setup

Clone the repository and enter the project folder:

```powershell
git clone https://github.com/flowbaka/property_operation_automation_pexus.git
cd property_operation_automation_pexus
```

Create and activate a virtual environment:

```powershell
python -m venv .propertyvenv
.\.propertyvenv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a PostgreSQL database named `propertyops_db`.

Copy `.env.example` to `.env` and enter your local database credentials:

```powershell
Copy-Item .env.example .env
```

Apply the database migrations:

```powershell
python -m alembic upgrade head
```

## Run FastAPI

```powershell
python -m uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run Streamlit

Open another terminal, activate the virtual environment and run:

```powershell
python -m streamlit run dashboard/dashboard.py
```

Dashboard:

```text
http://localhost:8501
```

## Run n8n

Start n8n in another terminal:

```powershell
npx.cmd n8n
```

Open:

```text
http://localhost:5678
```

Import the workflow from:

```text
n8n_workflows/Property_Operation_Workflow.json
```

The n8n workflow receives newly created lead data and calls the FastAPI follow-up-task endpoint.

## Application Flow

1. A customer lead is created through the FastAPI API.
2. The lead is stored in PostgreSQL.
3. FastAPI sends the lead data to an n8n webhook.
4. n8n creates a follow-up task through the API.
5. Streamlit displays the leads, tasks and operational metrics.

## Security

* Database credentials are stored in `.env`.
* `.env` is excluded from Git.
* `.env.example` contains only placeholder values.
* Real customer information should not be used during development.
