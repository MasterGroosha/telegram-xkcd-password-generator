from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot.i18n import resolve_locale, t
from bot.metrics import emit_metric

router = Router(name="start")
router.message.filter(CommandStart(), ~F.forward_origin)


@router.message()
async def cmd_start(
    message: Message,
) -> None:
    await emit_metric("command.start")
    locale = resolve_locale(message.from_user.language_code if message.from_user else None)
    await message.answer(
        text=t("start-message", locale=locale),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=t("btn-try-inline", locale=locale),
                        switch_inline_query_current_chat="",
                    )
                ]
            ]
        ),
    )
