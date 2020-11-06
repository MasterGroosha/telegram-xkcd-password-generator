import logging
from aiogram import Bot, Dispatcher
from configurator import config, check_config_file


# Configure logging
logging.basicConfig(level=logging.INFO)

if not check_config_file("config/config.ini"):
    exit("Error parsing config file. Exiting.")

if not config.general.token:
    exit("No token provided")

# Initialize bot and dispatcher
bot = Bot(token=config.general.token, parse_mode="HTML")
dp = Dispatcher(bot)
