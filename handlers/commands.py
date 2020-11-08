from aiogram import types
from misc import dp
from other.texts import strings, get_language
from other import dbworker, pwdgen, keyboards as kb


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(strings.get(get_language(message.from_user.language_code)).get("start"))


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(strings.get(get_language(message.from_user.language_code)).get("help"))


@dp.message_handler(commands=["settings"])
async def cmd_settings(message: types.Message):
    await message.answer(text=dbworker.get_settings_text(message.chat.id, message.from_user.language_code),
                         reply_markup=kb.make_settings_keyboard_for_user(dbworker.get_person(message.chat.id),
                                                                         message.from_user.language_code))


@dp.message_handler(commands=["generate"])
async def cmd_generate_custom(message: types.Message):
    await message.answer(text=f"<code>{pwdgen.generate_custom(message.chat.id)}</code>",
                         reply_markup=kb.make_regenerate_keyboard(message.from_user.language_code))


@dp.message_handler(commands=["generate_weak"])
async def cmd_generate_weak_password(message: types.Message):
    await message.answer(f"<code>{pwdgen.generate_weak_pwd()}</code>")


@dp.message_handler(commands=["generate_normal"])
async def cmd_generate_normal_password(message: types.Message):
    await message.answer(f"<code>{pwdgen.generate_normal_pwd()}</code>")


@dp.message_handler(commands=["generate_strong"])
async def cmd_generate_strong_password(message: types.Message):
    await message.answer(f"<code>{pwdgen.generate_strong_pwd()}</code>")


@dp.message_handler(commands=["generate_stronger"])
async def cmd_generate_stronger_password(message: types.Message):
    await message.answer(f"<code>{pwdgen.generate_stronger_pwd()}</code>")


@dp.message_handler(commands=["generate_insane"])
async def cmd_generate_insane_password(message: types.Message):
    await message.answer(f"<code>{pwdgen.generate_insane_pwd()}</code>")


@dp.message_handler()  # Default messages handler
async def default(message: types.Message):
    await cmd_generate_strong_password(message)
