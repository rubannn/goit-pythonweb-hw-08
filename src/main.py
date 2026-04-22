from fastapi import FastAPI

from src.api.contacts import router as contacts_router
from src.database.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    description="REST API for storing and managing contacts.",
    version="0.1.0",
)


@app.get("/", tags=["healthcheck"])
def read_root() -> dict[str, str]:
    return {"message": "Contacts API is running"}


app.include_router(contacts_router, prefix="/api")
