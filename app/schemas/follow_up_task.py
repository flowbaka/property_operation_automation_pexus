from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class FollowUpTaskCreate(BaseModel):
    """Information accepted when creating a task."""

    lead_id: int = Field(gt=0)

    title: str = Field(
        min_length=3,
        max_length=200,
    )

    due_at: datetime | None = None


class FollowUpTaskResponse(BaseModel):
    """Follow-up task information returned by the API."""

    id: int
    lead_id: int
    title: str
    status: str
    due_at: datetime | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)