from other.config import load_config
from pathlib import Path

if __name__ == '__main__':
    # First initialize and check our config
    try:
        load_config(Path.joinpath(Path(__file__).parent, "data/config/config.ini"))
    except ValueError as ex:
        exit(f"Error: {ex}")

    # Now load everything else
    from aiogram import executor
    from misc import dp
    import handlers

    executor.start_polling(dp, skip_updates=True)
