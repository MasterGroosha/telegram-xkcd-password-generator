from typing import Literal

from aiogram.filters.callback_data import CallbackData


class GenerateCallback(CallbackData, prefix="gen"):
    action: Literal[
        "word_minus", "word_plus", "toggle_delimiters", "toggle_edge", "regenerate", "delete"
    ]