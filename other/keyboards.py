from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from other.texts import all_strings, get_language
from .config import app_config, DBKeys
from .storage import get_data

cb_wordcount = CallbackData("word", "change")
cb_prefixes = CallbackData("prefixes", "action")
cb_separators = CallbackData("separators", "action")


async def make_settings_keyboard_for_user_async(state: FSMContext, lang_code: str) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    data = await get_data(state)
    wordcount_buttons = []
    wordcount = data.get(DBKeys.WORDS_COUNT.value)
    if wordcount > app_config.min_words:
        wordcount_buttons.append(types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("minusword"),
                                                            callback_data=cb_wordcount.new(change="minus")))
    if wordcount < app_config.max_words:
        wordcount_buttons.append(types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("plusword"),
                                                            callback_data=cb_wordcount.new(change="plus")))
    kb.add(*wordcount_buttons)

    if data.get(DBKeys.PREFIXES_SUFFIXES.value, True) is True:
        kb.add(types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("minuspref"),
                                          callback_data=cb_prefixes.new(action="disable")))
    else:
        kb.add(types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("pluspref"),
                                          callback_data=cb_prefixes.new(action="enable")))

    if data.get(DBKeys.SEPARATORS.value, True) is True:
        kb.add(types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("minussep"),
                                          callback_data=cb_separators.new(action="disable")))
    else:
        kb.add(types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("plussep"),
                                          callback_data=cb_separators.new(action="enable")))

    return kb


def make_regenerate_keyboard(lang_code):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text=all_strings.get(get_language(lang_code)).get("regenerate"),
                                     callback_data="regenerate")
    keyboard.add(btn)
    return keyboard
