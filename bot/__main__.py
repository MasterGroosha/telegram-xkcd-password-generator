import asyncio

import structlog
from aiogram import Bot, Dispatcher
from structlog.typing import FilteringBoundLogger

from bot.config import Settings
from bot.handlers import get_routers
from bot.logging_config import setup_logging
from bot.metrics import init_metrics
from bot.pwdgen import XKCDGenerator

logger: FilteringBoundLogger = structlog.get_logger()


async def main() -> None:
    settings = Settings()
    setup_logging(settings.logs)
    init_metrics(settings.logs.project_name)

    bot = Bot(
        token=settings.bot.token.get_secret_value(),
    )

    xkcd = XKCDGenerator(filename=settings.xkcd.wordfile)

    dp = Dispatcher(xkcdgen=xkcd)
    dp.include_routers(*get_routers())

    await logger.ainfo("Starting polling...")
    try:
        await dp.start_polling(bot)
    finally:
        await logger.ainfo("Bot stopped.")


asyncio.run(main())
