from contextlib import suppress

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.utils.exceptions import MessageNotModified

from bot.keyboards import make_regenerate_keyboard, make_settings_keyboard
from bot.localization import get_settings_string
from bot.common import cb_wordcount, cb_separators, cb_prefixes


async def regenerate_custom_password(call: types.CallbackQuery, state: FSMContext):
    """
    Generates a new custom password on button click

    :param call: Callback Query
    :param state: current user's state & data
    """
    pwd = call.bot.get("pwd")
    data = await state.get_data()
    new_password = pwd.custom(data.get("words_count"), data.get("separators"), data.get("prefixes_suffixes"))
    await call.message.edit_text(
        text=hcode(new_password),
        reply_markup=make_regenerate_keyboard(call.from_user.language_code)
    )


async def update_settings_message(call: types.CallbackQuery, data: dict):
    """
    Edits settings message text and keyboard

    :param call: Callback Query
    :param data: current user's state & data
    """
    config = call.bot.get("config")
    lang_code = call.from_user.language_code
    words_count = data.get("words_count")
    separators_enabled = data.get("separators")
    prefixes_enabled = data.get("prefixes_suffixes")
    new_settings_text = get_settings_string(lang_code, words_count, separators_enabled, prefixes_enabled)
    new_keyboard = make_settings_keyboard(config, lang_code, words_count, separators_enabled, prefixes_enabled)

    with suppress(MessageNotModified):
        await call.message.edit_text(new_settings_text, reply_markup=new_keyboard)
    await call.answer()


async def toggle_feature(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Toggle features like "separators" and "prefixes/suffixes"

    :param call: Callback Query
    :param callback_data: buttons data
    :param state: current user's state & data
    """
    new_value = callback_data["action"] == "enable"
    await state.update_data({callback_data["@"]: new_value})
    data = await state.get_data()
    await update_settings_message(call, data)


async def change_words_count(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Change number of words to generate in password

    :param call: Callback Query
    :param callback_data: buttons data
    :param state: current user's state & data
    """
    from bot.config_reader import Config
    config: Config = call.bot.get("config")
    data = await state.get_data()
    old_value = data.get("words_count", 3)

    if callback_data["change"] == "plus" and old_value < config.words.max:
        await state.update_data(words_count=old_value + 1)
    elif callback_data["change"] == "minus" and old_value > config.words.min:
        await state.update_data(words_count=old_value - 1)

    data = await state.get_data()  # Ask for updated dict
    await update_settings_message(call, data)


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(regenerate_custom_password, text="regenerate")
    dp.register_callback_query_handler(toggle_feature, cb_separators.filter(action=["disable", "enable"]))
    dp.register_callback_query_handler(toggle_feature, cb_prefixes.filter(action=["disable", "enable"]))
    dp.register_callback_query_handler(change_words_count, cb_wordcount.filter(change=["minus", "plus"]))
