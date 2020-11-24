from typing import Dict
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageNotModified
from misc import dp
from other import pwdgen, storage
from other import keyboards as kb
from other import texts


@dp.callback_query_handler(text="regenerate")
async def regenerate(call: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await call.message.edit_text(text=f"<code>{pwdgen.generate_custom(user_data)}</code>",
                                 reply_markup=kb.make_regenerate_keyboard(call.from_user.language_code))
    await call.answer()


@dp.callback_query_handler(kb.cb_wordcount.filter())
async def change_wordcount(call: types.CallbackQuery, callback_data: Dict[str, str], state: FSMContext):
    if callback_data["change"] == "minus":
        await storage.change_word_count(state, increase=False)
    elif callback_data["change"] == "plus":
        await storage.change_word_count(state, increase=True)
    else:
        return

    keyboard = await kb.make_settings_keyboard_for_user_async(state, call.from_user.language_code)
    user_data = await state.get_data()
    user_lang = texts.get_language(call.from_user.language_code)
    try:
        await call.message.edit_text(text=texts.get_settings_string(user_data, user_lang), reply_markup=keyboard)
    except MessageNotModified:
        pass
    await call.answer()


@dp.callback_query_handler(kb.cb_prefixes.filter())
async def toggle_prefixes(call: types.CallbackQuery, callback_data: Dict[str, str], state: FSMContext):
    if callback_data["action"] == "disable":
        await storage.toggle_feature(state, "prefixes_suffixes", False)
    elif callback_data["action"] == "enable":
        await storage.toggle_feature(state, "prefixes_suffixes", True)
    else:
        return

    keyboard = await kb.make_settings_keyboard_for_user_async(state, call.from_user.language_code)
    user_data = await state.get_data()
    user_lang = texts.get_language(call.from_user.language_code)
    try:
        await call.message.edit_text(text=texts.get_settings_string(user_data, user_lang), reply_markup=keyboard)
    except MessageNotModified:
        pass
    await call.answer()


@dp.callback_query_handler(kb.cb_separators.filter())
async def toggle_separators(call: types.CallbackQuery, callback_data: Dict[str, str], state: FSMContext):
    if callback_data["action"] == "disable":
        await storage.toggle_feature(state, "separators", False)
    elif callback_data["action"] == "enable":
        await storage.toggle_feature(state, "separators", True)
    else:
        return

    keyboard = await kb.make_settings_keyboard_for_user_async(state, call.from_user.language_code)
    user_data = await state.get_data()
    user_lang = texts.get_language(call.from_user.language_code)
    try:
        await call.message.edit_text(text=texts.get_settings_string(user_data, user_lang), reply_markup=keyboard)
    except MessageNotModified:
        pass
    await call.answer()
