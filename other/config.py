from configparser import ConfigParser
from dataclasses import dataclass
from xkcdpass import xkcd_password
from typing import List
from enum import Enum


class DBKeys(Enum):
    WORDS_COUNT = "words_count"
    PREFIXES_SUFFIXES = "prefixes_suffixes"
    SEPARATORS = "separators"


# Global config object
app_config = None


@dataclass
class BotConfig:
    words_file: str


@dataclass
class PwdConfig:
    min: int
    max: int


@dataclass
class DefaultValues:
    words_count: int
    prefixes_suffixes: bool
    separators: bool


@dataclass
class Config:
    bot: BotConfig = None
    pwd_words: PwdConfig = None
    default: DefaultValues = None
    wordlist: List[str] = None


def load_config(path: str):
    required_schema = {
        "general": ["words_file"],
        "pwd_words_count": ["min", "max"],
        "default": ["words_count", "prefixes_suffixes", "separators"]
    }
    cfg = ConfigParser()
    cfg.read(path)
    sections = cfg.sections()
    if len(sections) == 0:
        raise ValueError("config file missing, empty, or contains no sections, e.g. [bot]")
    # Check all required sections and options are present in config
    for section in required_schema:
        if section not in sections:
            raise ValueError(f"missing section {section} in config file")
        for option in required_schema[section]:
            if option not in cfg[section]:
                raise ValueError(f'missing required option "{option}" in section "{section}" in config file')

    # All checks passed, time to init objects
    global app_config
    app_config = Config(
        bot=BotConfig(
            words_file=cfg["general"]["words_file"]
        ),
        pwd_words=PwdConfig(
            min=cfg.getint("pwd_words_count", "min"),
            max=cfg.getint("pwd_words_count", "max"),
        ),
        default=DefaultValues(
            words_count=cfg.getint("default", "words_count"),
            prefixes_suffixes=cfg.getboolean("default", "prefixes_suffixes"),
            separators=cfg.getboolean("default", "separators")
        )
    )
    app_config.wordlist = xkcd_password.generate_wordlist(wordfile=app_config.bot.words_file,
                                                          min_length=4, max_length=10, valid_chars="[a-z]")
    return app_config
