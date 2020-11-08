from configparser import ConfigParser
from dataclasses import dataclass
from xkcdpass import xkcd_password
from tinydb import TinyDB
from typing import List


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class BotConfig:
    token: str
    db_file: str
    words_file: str


@dataclass
class PwdConfig:
    min: int
    max: int


@dataclass
class Config(metaclass=Singleton):
    bot: BotConfig = None
    pwd_words: PwdConfig = None
    wordlist: List[str] = None
    tinydb = None

    # @classmethod
    # def get_instance(cls):
    #     return Config()


def load_config(path: str):
    required_schema = {
        "general": ["token", "db_file", "words_file"],
        "pwd_words_count": ["min", "max"]
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
    config = Config(
        bot=BotConfig(
            token=cfg["general"]["token"],
            db_file=cfg["general"]["db_file"],
            words_file=cfg["general"]["words_file"]
        ),
        pwd_words=PwdConfig(
            min=cfg.getint("pwd_words_count", "min"),
            max=cfg.getint("pwd_words_count", "max"),
        )
    )
    config.wordlist = xkcd_password.generate_wordlist(wordfile=config.bot.words_file,
                                                      min_length=4, max_length=10, valid_chars="[a-z]")
    config.tinydb = TinyDB(config.bot.db_file)
    return config
