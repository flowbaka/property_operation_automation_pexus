from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class FollowUpTask(Base):
    __tablename__ = "follow_up_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect this task to a lead
    lead_id: Mapped[int] = mapped_column(
        ForeignKey(
            "leads.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
    )

    due_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )