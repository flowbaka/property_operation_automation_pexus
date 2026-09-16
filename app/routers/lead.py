from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Lead
from app.schemas import LeadCreate, LeadResponse, LeadStatusUpdate
from sqlalchemy import select               
from app.services.n8n import trigger_new_lead_workflow

router = APIRouter(
    prefix="/leads",
    tags=["Leads"],
)


@router.post("/", response_model=LeadResponse, status_code=status.HTTP_201_CREATED)
def create_lead(
    lead_data: LeadCreate,
    background_tasks: BackgroundTasks,
    database_session: Session = Depends(get_db),
):
    new_lead = Lead(**lead_data.model_dump())

    database_session.add(new_lead)
    database_session.commit()
    database_session.refresh(new_lead)

    background_tasks.add_task(
        trigger_new_lead_workflow,
        {
            "event": "lead.created",
            "lead_id": new_lead.id,
            "name": new_lead.name,
            "email": new_lead.email,
            "phone": new_lead.phone,
            "message": new_lead.message,
            "source": new_lead.source,
        },
    )

    return new_lead



@router.get(
    "",
    response_model=list[LeadResponse],
)
def get_all_leads(
    database_session: Session = Depends(get_db),
):
    """Return all leads, newest first."""

    statement = select(Lead).order_by(Lead.created_at.desc())

    leads = database_session.scalars(statement).all()

    return leads


@router.get(
    "/{lead_id}",
    response_model=LeadResponse,
)
def get_lead(
    lead_id: int,
    database_session: Session = Depends(get_db),
):
    """Return one lead using its ID."""

    lead = database_session.get(Lead, lead_id)

    if lead is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )

    return lead


@router.patch(
    "/{lead_id}/status",
    response_model=LeadResponse,
)
def update_lead_status(
    lead_id: int,
    status_data: LeadStatusUpdate,
    database_session: Session = Depends(get_db),
):
    """Update the progress status of a lead."""

    lead = database_session.get(Lead, lead_id)

    if lead is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )

    lead.status = status_data.status

    database_session.commit()
    database_session.refresh(lead)

    return lead