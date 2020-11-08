from typing import Dict
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from other.config import Config
from other.texts import strings, get_language

cb_wordcount = CallbackData("word", "change")
cb_prefixes = CallbackData("prefixes", "action")
cb_separators = CallbackData("separators", "action")


def make_settings_keyboard_for_user(user: Dict, lang_code: str):
    """
    Prepare keyboard for user based on his settings

    :param user: Info about user
    :param lang_code: User's language code
    :return: Inline Keyboard object
    """
    kb = types.InlineKeyboardMarkup()
    config = Config()

    wrds_lst = []
    if user["word_count"] >= (config.pwd_words.min + 1):
        wrds_lst.append(types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("minusword"),
                                                   callback_data=cb_wordcount.new(change="minus")))
    if user["word_count"] <= (config.pwd_words.max - 1):
        wrds_lst.append(types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("plusword"),
                                                   callback_data=cb_wordcount.new(change="plus")))
    kb.add(*wrds_lst)

    if user["prefixes"]:
        kb.add(types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("minuspref"),
                                          callback_data=cb_prefixes.new(action="disable")))
    else:
        kb.add(types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("pluspref"),
                                          callback_data=cb_prefixes.new(action="enable")))

    if user["separators"]:
        kb.add(types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("minussep"),
                                          callback_data=cb_separators.new(action="disable")))
    else:
        kb.add(types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("plussep"),
                                          callback_data=cb_separators.new(action="enable")))
    return kb


def make_regenerate_keyboard(lang_code):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text=strings.get(get_language(lang_code)).get("regenerate"),
                                     callback_data="regenerate")
    keyboard.add(btn)
    return keyboard
