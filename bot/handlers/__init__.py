from aiogram import F, Router

from . import (
    start,
    generate,
    inline_mode,
)


def get_routers() -> list[Router]:
    return [
        start.router,
        generate.router,
        inline_mode.router,
    ]

