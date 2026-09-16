from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import FollowUpTask, Lead
from app.schemas import FollowUpTaskCreate, FollowUpTaskResponse
from app.schemas import (
    FollowUpTaskCreate,
    FollowUpTaskResponse,
    FollowUpTaskStatusUpdate,
)


router = APIRouter(
    prefix="/follow-up-tasks",
    tags=["Follow-up Tasks"],
)


@router.post(
    "",
    response_model=FollowUpTaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_follow_up_task(
    task_data: FollowUpTaskCreate,
    database_session: Session = Depends(get_db),
):
    """Create a follow-up task for an existing lead."""

    lead = database_session.get(Lead, task_data.lead_id)

    if lead is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )

    new_task = FollowUpTask(**task_data.model_dump())

    database_session.add(new_task)
    database_session.commit()
    database_session.refresh(new_task)

    return new_task


@router.get(
    "",
    response_model=list[FollowUpTaskResponse],
)
def get_all_follow_up_tasks(
    database_session: Session = Depends(get_db),
):
    """Return all follow-up tasks, newest first."""

    statement = select(FollowUpTask).order_by(
        FollowUpTask.created_at.desc()
    )

    tasks = database_session.scalars(statement).all()

    return tasks


@router.patch(
    "/{task_id}/status",
    response_model=FollowUpTaskResponse,
)
def update_follow_up_task_status(
    task_id: int,
    status_data: FollowUpTaskStatusUpdate,
    database_session: Session = Depends(get_db),
):
    """Update a follow-up task's status."""

    task = database_session.get(FollowUpTask, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Follow-up task not found",
        )

    task.status = status_data.status

    database_session.commit()
    database_session.refresh(task)

    return task