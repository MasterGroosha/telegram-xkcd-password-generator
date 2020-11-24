from configparser import ConfigParser
from dataclasses import dataclass
from xkcdpass import xkcd_password
from enum import Enum


class DBKeys(Enum):
    WORDS_COUNT = "words_count"
    PREFIXES_SUFFIXES = "prefixes_suffixes"
    SEPARATORS = "separators"


# Global config object
app_config = None


@dataclass
class Settings:
    wordfile: str
    min_words: int
    max_words: int
    default_words: int = None
    default_pref_suf: bool = None
    default_separators: bool = None


def load_config(path: str):
    key_settings = "settings"
    required_settings = ("wordfile", "min_words", "max_words",
                         "default_words", "default_pref_suf", "default_separators")
    cfg = ConfigParser()
    cfg.read(path)
    sections = cfg.sections()
    if key_settings not in sections:
        raise ValueError(f"missing section [{key_settings}] in config file")
    for option in required_settings:
        if option not in cfg[key_settings]:
            raise ValueError(f'missing required option "{option}" in config file')

    # All checks passed, time to init objects
    global app_config
    app_config = Settings(
        wordfile=cfg[key_settings]["wordfile"],
        min_words=cfg.getint(key_settings, "min_words"),
        max_words=cfg.getint(key_settings, "max_words")
    )
    app_config.__setattr__(DBKeys.WORDS_COUNT.value, cfg.getint(key_settings, "default_words"))
    app_config.__setattr__(DBKeys.PREFIXES_SUFFIXES.value, cfg.getboolean(key_settings, "default_pref_suf"))
    app_config.__setattr__(DBKeys.SEPARATORS.value, cfg.getboolean(key_settings, "default_separators"))

    app_config.words = xkcd_password.generate_wordlist(wordfile=app_config.wordfile,
                                                       min_length=4, max_length=10, valid_chars="[a-z]")
    return app_config
