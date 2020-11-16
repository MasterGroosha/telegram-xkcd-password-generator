from other.config import load_config
from pathlib import Path
import logging


# noinspection PyUnresolvedReferences
if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Initialize and check our config
    try:
        load_config(Path.joinpath(Path(__file__).parent, "config/config.ini"))
    except ValueError as ex:
        exit(f"Error: {ex}")

    # Now load everything else
    from aiogram import executor
    from misc import dp
    import handlers

    executor.start_polling(dp, skip_updates=True, on_startup=handlers.commands.register_bot_commands)
