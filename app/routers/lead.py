from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Lead
from app.schemas import LeadCreate, LeadResponse


router = APIRouter(
    prefix="/leads",
    tags=["Leads"],
)


@router.post(
    "",
    response_model=LeadResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_lead(
    lead_data: LeadCreate,
    database_session: Session = Depends(get_db),
):
    """Validate and save a new customer enquiry."""

    new_lead = Lead(**lead_data.model_dump())

    database_session.add(new_lead)
    database_session.commit()
    database_session.refresh(new_lead)

    return new_lead