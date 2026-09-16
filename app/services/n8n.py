import logging

import httpx

from app.config import settings


logger = logging.getLogger(__name__)


async def trigger_new_lead_workflow(payload: dict) -> None:
    """Send a newly created lead to the n8n workflow."""

    if not settings.N8N_WEBHOOK_URL:
        return

    headers = {}

    if settings.N8N_WEBHOOK_TOKEN is not None:
        headers["X-Webhook-Token"] = (
            settings.N8N_WEBHOOK_TOKEN.get_secret_value()
        )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                settings.N8N_WEBHOOK_URL,
                json=payload,
                headers=headers,
            )
            response.raise_for_status()

    except httpx.HTTPError:
        logger.exception("Could not trigger the n8n lead workflow")