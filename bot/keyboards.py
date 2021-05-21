from aiogram import types
from bot.localization import get_string
from bot.config_reader import Config
from bot.common import cb_wordcount, cb_separators, cb_prefixes


def make_settings_keyboard(
        config: Config,
        language: str,
        current_wordcount: int,
        separators_enabled: bool,
        prefixes_enabled: bool
) -> types.InlineKeyboardMarkup:
    """
    Returns inline keyboard for settings message

    :param config: bot's Config instance
    :param language: language code taken from Message object
    :param current_wordcount: current number of words in password to generate
    :param separators_enabled: bool, whether words must be separated with delimiters
    :param prefixes_enabled: bool, whether there must be chars from delimiters list in front and in back
    :return: inline keyboard object for current settings
    """
    kb = types.InlineKeyboardMarkup()

    # Add wordcount buttons row (has 1 or 2 buttons)
    wordcount_buttons = []
    if current_wordcount > config.words.min:
        wordcount_buttons.append(
            types.InlineKeyboardButton(
                text=get_string(language, "minusword"),
                callback_data=cb_wordcount.new(change="minus")
            )
        )
    if current_wordcount < config.words.max:
        wordcount_buttons.append(
            types.InlineKeyboardButton(
                text=get_string(language, "plusword"),
                callback_data=cb_wordcount.new(change="plus")
            )
        )
    kb.add(*wordcount_buttons)

    # Add toggles for prefixes/suffixes and separators
    pref_string, pref_cb = ("minuspref", "disable") if prefixes_enabled else ("pluspref", "enable")
    kb.add(types.InlineKeyboardButton(
        text=get_string(language, pref_string),
        callback_data=cb_prefixes.new(action=pref_cb))
    )

    sep_string, sep_cb = ("minussep", "disable") if separators_enabled else ("plussep", "enable")
    kb.add(types.InlineKeyboardButton(
        text=get_string(language, sep_string),
        callback_data=cb_separators.new(action=sep_cb))
    )
    return kb


def make_regenerate_keyboard(language: str):
    """
    Returns a one-button inline keyboard with localized "Regenerate" text

    :param language: language code taken from Message object
    :return: a one-button inline keyboard with localized "Regenerate" text
    """
    button = types.InlineKeyboardButton(
        text=get_string(language, "regenerate"),
        callback_data="regenerate"
    )
    return types.InlineKeyboardMarkup(inline_keyboard=[[button]])
