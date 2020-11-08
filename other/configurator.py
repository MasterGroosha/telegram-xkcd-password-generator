from pathlib import Path

try:
    from data.config import config
except ImportError:
    exit("File config.py not found in data/config/ directory. Please make sure this file exists and is readable.")


def check():
    if len(config.token) == 0:
        raise ValueError("Error: bot's token is empty!")

    print(Path.joinpath(Path().absolute(), config.db_file))
    if not Path.joinpath(Path().absolute(), config.db_file).exists():
        raise ValueError(f"Error: missing database file at '{config.db_file}'")

    if not Path.joinpath(Path().absolute(), config.words_file).exists():
        raise ValueError(f"Error: missing words file at '{config.words_file}'")

    if config.words_min < 1 or config.words_max < 1:
        raise ValueError("Error: number of min/max words cannot be less than 1")
    if config.words_min > config.words_max:
        raise ValueError("Error: words_max cannot be less than words_min")

    return
