import logging
from aiogram import Bot, Dispatcher
import data.config.config as config


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=config.token, parse_mode="HTML")
dp = Dispatcher(bot)
