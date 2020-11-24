from aiogram import types
from aiogram.dispatcher import FSMContext
from misc import dp
from other import texts
from other import pwdgen, keyboards as kb
from other.storage import get_data


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message, state: FSMContext):
    # Initialize values for new user or update possible missing values for existing one
    await get_data(state)

    await message.answer(texts.all_strings.get(texts.get_language(message.from_user.language_code)).get("start"))


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(texts.all_strings.get(texts.get_language(message.from_user.language_code)).get("help"))


@dp.message_handler(commands=["settings"])
async def cmd_settings(message: types.Message, state: FSMContext):
    user_data = await get_data(state)
    keyboard = await kb.make_settings_keyboard_for_user_async(state, message.from_user.language_code)
    user_lang = texts.get_language(message.from_user.language_code)
    await message.answer(text=texts.get_settings_string(user_data, user_lang), reply_markup=keyboard)


@dp.message_handler(commands=["generate"])
async def cmd_generate_custom(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(text=f"<code>{pwdgen.generate_custom(data)}</code>",
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


@dp.message_handler(commands=["generate_insane"])
async def cmd_generate_insane_password(message: types.Message):
    await message.answer(f"<code>{pwdgen.generate_insane_pwd()}</code>")


@dp.message_handler()  # Default messages handler
async def default(message: types.Message):
    await cmd_generate_normal_password(message)


async def register_bot_commands(dispatcher):
    commands = [
        types.BotCommand(command="generate", description="custom password, configured in /settings"),
        types.BotCommand(command="generate_weak", description="2 words, no digits"),
        types.BotCommand(command="generate_normal", description="3 words, random uppercase, separated by numbers"),
        types.BotCommand(command="generate_strong", description="4 words, random uppercase, no separators"),
        types.BotCommand(command="generate_insane", description="3 words, prefixes, suffixes, separators, random uppercase"),
        types.BotCommand(command="settings", description="customize /generate results"),
        types.BotCommand(command="help", description="help and source code")
    ]
    await dp.bot.set_my_commands(commands)
