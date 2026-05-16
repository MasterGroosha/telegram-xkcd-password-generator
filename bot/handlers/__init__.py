from aiogram import Router

from . import (
    errors,
    generate,
    inline_mode,
    start,
)


def get_routers() -> list[Router]:
    return [
        start.router,
        generate.router,
        inline_mode.router,
        errors.router,
    ]
