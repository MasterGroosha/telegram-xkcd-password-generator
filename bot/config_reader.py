from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class Bot:
    token: str


@dataclass
class Words:
    wordfile: str
    min: int
    max: int
    default: int
    pref_suf: bool
    separators: bool


@dataclass
class Redis:
    host: str


@dataclass
class Config:
    bot: Bot
    words: Words
    redis: Redis


def load_config(path: str):
    cfg = ConfigParser()
    cfg.read(path)

    return Config(
        bot=Bot(token=cfg.get("bot", "token")),
        words=Words(
            wordfile=cfg.get("words", "wordfile"),
            min=cfg.getint("words", "min"),
            max=cfg.getint("words", "max"),
            default=cfg.getint("words", "default"),
            pref_suf=cfg.getboolean("words", "pref_suf"),
            separators=cfg.getboolean("words", "separators")
        ),
        redis=Redis(host=cfg.get("redis", "host"))
    )
