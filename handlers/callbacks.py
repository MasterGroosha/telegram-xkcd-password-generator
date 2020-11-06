from typing import Dict
from aiogram import types
from misc import dp
import pwdgen
import dbworker
import keyboards.inline_kb as kb


@dp.callback_query_handler(text="regenerate")
async def regenerate(call: types.CallbackQuery):
    await call.message.edit_text(text=f"<code>{pwdgen.generate_custom(call.from_user.id)}</code>",
                                 reply_markup=kb.make_regenerate_keyboard(call.from_user.language_code))
    await call.answer()


@dp.callback_query_handler(kb.cb_wordcount.filter())
async def change_wordcount(call: types.CallbackQuery, callback_data: Dict[str, str]):
    if callback_data["change"] == "minus":
        dbworker.change_word_count(call.from_user.id, increase=False)
    elif callback_data["change"] == "plus":
        dbworker.change_word_count(call.from_user.id, increase=True)
    else:
        return

    await call.message.edit_text(text=dbworker.get_settings_text(call.from_user.id, call.from_user.language_code),
                                 reply_markup=kb.make_settings_keyboard_for_user(dbworker.get_person(call.from_user.id),
                                                                                 call.from_user.language_code))
    await call.answer()


@dp.callback_query_handler(kb.cb_prefixes.filter())
async def toggle_prefixes(call: types.CallbackQuery, callback_data: Dict[str, str]):
    if callback_data["action"] == "disable":
        dbworker.change_prefixes(call.from_user.id, enable_prefixes=False)
    elif callback_data["action"] == "enable":
        dbworker.change_prefixes(call.from_user.id, enable_prefixes=True)
    else:
        return

    await call.message.edit_text(text=dbworker.get_settings_text(call.from_user.id, call.from_user.language_code),
                                 reply_markup=kb.make_settings_keyboard_for_user(dbworker.get_person(call.from_user.id),
                                                                                 call.from_user.language_code))
    await call.answer()


@dp.callback_query_handler(kb.cb_separators.filter())
async def toggle_separators(call: types.CallbackQuery, callback_data: Dict[str, str]):
    if callback_data["action"] == "disable":
        dbworker.change_separators(call.from_user.id, enable_separators=False)
    elif callback_data["action"] == "enable":
        dbworker.change_separators(call.from_user.id, enable_separators=True)
    else:
        return

    await call.message.edit_text(text=dbworker.get_settings_text(call.from_user.id, call.from_user.language_code),
                                 reply_markup=kb.make_settings_keyboard_for_user(dbworker.get_person(call.from_user.id),
                                                                                 call.from_user.language_code))
    await call.answer()
