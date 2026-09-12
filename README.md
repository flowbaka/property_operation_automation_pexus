# PropertyOps AI

A property sales and business automation project.

## Planned features

- Customer enquiries
- Follow-up tasks
- Document RAG (retrieval-augmented generation)
- n8n automation
- Marketing and financial analysis
- Streamlit dashboard

## Current progress

The initial FastAPI application is available with this endpoint:

- `GET /` returns `{"message": "PropertyOps AI API is running"}`.

## Run locally

Start the development server from the project root:

```bash
python -m uvicorn app.main:app --reload
```

Open the API at [http://127.0.0.1:8000](http://127.0.0.1:8000) or view the interactive documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Initial stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
