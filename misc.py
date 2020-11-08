import logging
from aiogram import Bot, Dispatcher
from other.config import Config


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
config = Config()
bot = Bot(token=config.bot.token, parse_mode="HTML")
dp = Dispatcher(bot)
