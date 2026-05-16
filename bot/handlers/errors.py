import structlog
from aiogram import Router
from aiogram.types import ErrorEvent
from structlog.types import FilteringBoundLogger

router = Router()

logger: FilteringBoundLogger = structlog.get_logger()


@router.error()
async def error_handler(event: ErrorEvent):
    await logger.aexception(
        f"Unhandled exception",
        incoming_update=event.update.model_dump(),
        exception_type=event.exception.__class__.__name__,
        exception_message=str(event.exception),
        kind="exception",
    )
