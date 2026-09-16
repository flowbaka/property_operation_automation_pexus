from fastapi import FastAPI

from app.routers.lead import router as lead_router
from app.routers.follow_up_task import router as follow_up_task_router


app = FastAPI(
    title="PropertyOps AI",
    description="Property sales and business automation API",
    version="0.1.0",
)


app.include_router(lead_router)
app.include_router(follow_up_task_router)


@app.get("/")
def root():
    return {"message": "PropertyOps AI API is running"}