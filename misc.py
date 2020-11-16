from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from other.config import app_config


# Initialize bot and dispatcher
bot = Bot(token=app_config.bot.token, parse_mode="HTML")
dp = Dispatcher(bot, storage=RedisStorage2(host="redis"))
