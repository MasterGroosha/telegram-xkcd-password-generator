import asyncio
import logging
from os.path import join

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from bot.config_reader import load_config
from bot.pwdgen import XKCD
from bot.handlers.commands import register_commands
from bot.handlers.callbacks import register_callbacks
from bot.handlers.inline_mode import register_inline_mode


async def set_commands(dp: Dispatcher):
    """
    Here we setup bot commands to make them visible in Telegram UI
    """
    bot_commands = [
        BotCommand(command="generate", description="Custom password, configured in /settings"),
        BotCommand(command="generate_weak", description="2 words, no digits"),
        BotCommand(command="generate_normal", description="3 words, random uppercase, separated by numbers"),
        BotCommand(command="generate_strong", description="4 words, random uppercase, random separators"),
        BotCommand(command="settings", description="customize /generate results"),
        BotCommand(command="help", description="Help and source code")
    ]
    await dp.bot.set_my_commands(bot_commands)


def get_handled_updates_list(dp: Dispatcher) -> list:
    """
    Here we collect only the needed updates for bot based on already registered handlers types.
    This way Telegram doesn't send unwanted updates and bot doesn't have to proceed them.
    :param dp: Dispatcher
    :return: a list of registered handlers types
    """
    available_updates = (
        "callback_query_handlers", "channel_post_handlers", "chat_member_handlers",
        "chosen_inline_result_handlers", "edited_channel_post_handlers", "edited_message_handlers",
        "inline_query_handlers", "message_handlers", "my_chat_member_handlers", "poll_answer_handlers",
        "poll_handlers", "pre_checkout_query_handlers", "shipping_query_handlers"
    )
    return [item.replace("_handlers", "") for item in available_updates
            if len(dp.__getattribute__(item).handlers) > 0]


async def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config(join("config", "config.ini"))
    xkcd = XKCD(config.words.wordfile)
    bot = Bot(token=config.bot.token, parse_mode="HTML")
    bot["pwd"] = xkcd
    bot["config"] = config
    dp = Dispatcher(bot, storage=RedisStorage2(host=config.redis.host))

    # Register handlers
    register_commands(dp)
    register_callbacks(dp)
    register_inline_mode(dp)

    await set_commands(dp)

    logging.info("Starting bot...")
    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await bot.close()

asyncio.run(main())
