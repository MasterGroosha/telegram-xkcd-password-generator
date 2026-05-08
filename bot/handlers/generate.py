import base64
import html
import json
import re

from aiogram import Router
from aiogram.enums import ParseMode, ButtonStyle
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    CopyTextButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.callback_factories import GenerateCallback
from bot.i18n import resolve_locale, t
from bot.metrics import emit_metric
from bot.pwdgen import XKCDGenerator

router = Router(name="generate")

_MIN_WORDS = 2
_MAX_WORDS = 5


def encode(payload: dict) -> str:
    b64 = base64.urlsafe_b64encode(
        json.dumps(payload, separators=(",", ":")).encode()
    ).decode().rstrip("=")
    return f'<a href="http://127.0.0.1/?d={b64}">​</a>'


def decode(url: str) -> dict | None:
    match = re.search(r'http://127\.0\.0\.1/\?d=([\w-]+)', url)
    if not match:
        return None
    b64 = match.group(1)
    b64 += "=" * (-len(b64) % 4)
    try:
        return json.loads(base64.urlsafe_b64decode(b64).decode())
    except Exception:
        return None


def extract_payload(message: Message) -> dict | None:
    if not message.entities:
        return None
    for entity in reversed(message.entities):
        if entity.type == "text_link":
            return decode(entity.url)
    return None


def _state(val: bool, locale: str) -> str:
    return t("state-enabled" if val else "state-disabled", locale=locale)


def build_password_text(password: str, params: dict, locale: str) -> str:
    text = t(
        "generate-message",
        locale=locale,
        word_count=params["word_count"],
        delimiters=html.escape(_state(params["delimiters"], locale)),
        edge_delimiters=html.escape(_state(params["edge_delimiters"], locale)),
        password=html.escape(password),
    )
    return text + encode(params)


def build_xkcd_keyboard(params: dict, password: str, locale: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    word_count = params["word_count"]

    row1 = []
    if word_count > _MIN_WORDS:
        row1.append(InlineKeyboardButton(
            text=t("btn-word-minus", locale=locale),
            callback_data=GenerateCallback(action="word_minus").pack(),
        ))
    if word_count < _MAX_WORDS:
        row1.append(InlineKeyboardButton(
            text=t("btn-word-plus", locale=locale),
            callback_data=GenerateCallback(action="word_plus").pack(),
        ))
    if row1:
        builder.row(*row1)

    delimiter_key = "btn-hide-delimiters" if params["delimiters"] else "btn-show-delimiters"
    builder.row(InlineKeyboardButton(
        text=t(delimiter_key, locale=locale),
        callback_data=GenerateCallback(action="toggle_delimiters").pack(),
    ))

    edge_key = "btn-remove-edge" if params["edge_delimiters"] else "btn-add-edge"
    builder.row(InlineKeyboardButton(
        text=t(edge_key, locale=locale),
        callback_data=GenerateCallback(action="toggle_edge").pack(),
    ))

    builder.row(InlineKeyboardButton(
        text=t("btn-regenerate", locale=locale),
        callback_data=GenerateCallback(action="regenerate").pack(),
    ))

    builder.row(InlineKeyboardButton(
        text=t("btn-copy-password", locale=locale),
        copy_text=CopyTextButton(text=password),
    ))

    builder.row(InlineKeyboardButton(
        text=t("btn-delete", locale=locale),
        callback_data=GenerateCallback(action="delete").pack(),
        style=ButtonStyle.DANGER,
    ))

    return builder.as_markup()


@router.message(Command("generate"))
async def cmd_generate(
        message: Message,
        xkcdgen: XKCDGenerator,
) -> None:
    await emit_metric("command.generate")
    locale = resolve_locale(message.from_user.language_code if message.from_user else None)
    params = {
        "type": "normal",
        "word_count": 3,
        "delimiters": True,
        "edge_delimiters": False,
    }
    password = xkcdgen.custom(
        word_count=params["word_count"],
        separators=params["delimiters"],
        prefixes=params["edge_delimiters"],
    )
    await message.answer(
        text=build_password_text(password, params, locale),
        parse_mode=ParseMode.HTML,
        reply_markup=build_xkcd_keyboard(params, password, locale),
    )


@router.callback_query(GenerateCallback.filter())
async def cb_xkcd(
        callback: CallbackQuery,
        xkcdgen: XKCDGenerator,
        callback_data: GenerateCallback,
) -> None:
    locale = resolve_locale(callback.from_user.language_code)
    params = extract_payload(callback.message)
    if params is None:
        await callback.answer()
        return

    action = callback_data.action

    if action == "delete":
        try:
            await callback.message.delete()
        except Exception:
            await callback.answer(t("delete-failed", locale=locale), show_alert=True)
        return

    if action == "word_minus":
        params["word_count"] = max(_MIN_WORDS, params["word_count"] - 1)
    elif action == "word_plus":
        params["word_count"] = min(_MAX_WORDS, params["word_count"] + 1)
    elif action == "toggle_delimiters":
        params["delimiters"] = not params["delimiters"]
    elif action == "toggle_edge":
        params["edge_delimiters"] = not params["edge_delimiters"]
    # "regenerate" — params unchanged, new password generated below

    password = xkcdgen.custom(
        word_count=params["word_count"],
        separators=params["delimiters"],
        prefixes=params["edge_delimiters"],
    )
    await callback.message.edit_text(
        text=build_password_text(password, params, locale),
        parse_mode=ParseMode.HTML,
        reply_markup=build_xkcd_keyboard(params, password, locale),
    )
    await callback.answer()
