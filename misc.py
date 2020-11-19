from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from os import getenv
from sys import exit

token = getenv("BOT_TOKEN", None)
if not token:
    exit("No bot token provided, exiting...")

# Initialize bot and dispatcher
bot = Bot(token=token, parse_mode="HTML", validate_token=True)
dp = Dispatcher(bot, storage=RedisStorage2(host="redis"))
