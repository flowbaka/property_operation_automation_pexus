from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Literal

class LeadStatusUpdate(BaseModel):
    """Status accepted when updating a lead."""

    status: Literal[
        "new",
        "contacted",
        "qualified",
        "closed",
    ]

class LeadCreate(BaseModel):
    """Information accepted when someone submits an enquiry."""

    name: str = Field(
        min_length=2,
        max_length=120,
    )

    email: EmailStr

    phone: str | None = Field(
        default=None,
        max_length=30,
    )

    message: str = Field(
        min_length=5,
        max_length=2000,
    )

    source: str = Field(
        default="website",
        min_length=2,
        max_length=50,
    )


class LeadResponse(BaseModel):
    """Information returned by the API."""

    id: int
    name: str
    email: EmailStr
    phone: str | None
    message: str
    source: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)