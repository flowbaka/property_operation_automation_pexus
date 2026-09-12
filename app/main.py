from fastapi import FastAPI


# Create the API application and publish its metadata in the generated docs.
app = FastAPI(
    title="PropertyOps AI",
    description="Property sales and business automation API",
    version="0.1.0",
)


# Provide a simple health check for clients and deployment tooling.
@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "PropertyOps AI API is running"}
