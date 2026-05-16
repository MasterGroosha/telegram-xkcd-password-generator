import html

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from bot.i18n import resolve_locale, t
from bot.metrics import emit_metric
from bot.pwdgen import XKCDGenerator

router = Router(name="inline_mode")

_THUMB_BASE = (
    "https://raw.githubusercontent.com/MasterGroosha/"
    "telegram-xkcd-password-generator/master/img/pwd_{color}.png"
)


def build_inline_message_text(password: str, user_text: str) -> str:
    text = f"<code>{html.escape(password)}</code>"
    if user_text:
        text += f"\n\n{html.escape(user_text)}"
    return text


def build_inline_description(description_key: str, user_text: str, locale: str) -> str:
    if user_text:
        return user_text
    return t(description_key, locale=locale)


@router.inline_query()
async def inline_handler(query: InlineQuery, xkcdgen: XKCDGenerator) -> None:
    locale = resolve_locale(query.from_user.language_code if query.from_user else None)
    user_text = query.query.strip()
    if not user_text:
        await emit_metric("inline.open")

    data = [
        {
            "title_key": "inline-weak-title",
            "description_key": "inline-weak-description",
            "password_func": xkcdgen.weak,
            "thumb_color": "red",
        },
        {

            "title_key": "inline-normal-title",
            "description_key": "inline-normal-description",
            "password_func": xkcdgen.normal,
            "thumb_color": "yellow",
        },
        {
            "title_key": "inline-strong-title",
            "description_key": "inline-strong-description",
            "password_func": xkcdgen.strong,
            "thumb_color": "green",
        },
    ]

    results = []
    for index, item in enumerate(data):
        password = item["password_func"]()
        results.append(
            InlineQueryResultArticle(
                id=str(index),
                title=t(item["title_key"], locale=locale),
                description=build_inline_description(
                    item["description_key"], user_text, locale
                ),
                input_message_content=InputTextMessageContent(
                    message_text=build_inline_message_text(password, user_text),
                    parse_mode=ParseMode.HTML,
                ),
                thumbnail_url=_THUMB_BASE.format(color=item["thumb_color"]),
                thumbnail_height=64,
                thumbnail_width=64,
            )
        )

    await query.answer(results, cache_time=1, is_personal=True)
