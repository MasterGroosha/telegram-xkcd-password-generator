from functools import partial
from random import choice
from xkcdpass import xkcd_password


class XKCDGenerator:
    delimiters_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    delimiters_full = ["!", "$", "%", "^", "&", "*", "-", "_", "+", "=",
                       ":", "|", "~", "?", "/", ".", ";"] + delimiters_numbers

    def __init__(self, filename: str):
        self.wordlist = xkcd_password.generate_wordlist(
            wordfile=filename, valid_chars="[a-z]", min_length=4, max_length=10,
        )
        self._generate_password = partial(
            xkcd_password.generate_xkcdpassword,
            wordlist=self.wordlist,
        )

    def weak(self):
        # 2 words, no separators between words
        return self._generate_password(
            numwords=2,
            delimiter="",
        )

    def normal(self):
        # 3 words, random CAPITALIZATION, random number as separator between words
        return self._generate_password(
            numwords=3,
            case="random",
            random_delimiters=True,
            valid_delimiters=self.delimiters_numbers,
        )

    def strong(self):
        # Same as normal_pwd, but 4 words
        return self._generate_password(
            numwords=4,
            case="random",
            random_delimiters=True,
            valid_delimiters=self.delimiters_full,
        )

    def custom(self, word_count: int, separators: bool, prefixes: bool):
        """
        Custom password generation

        :param word_count: number of words in password
        :param separators: bool, whether words must be separated with delimiters
        :param prefixes: bool, whether there must be chars from delimiters list in front and in back
        :return: generated custom password
        """
        pwd = self._generate_password(
            numwords=word_count,
            case="random",
            delimiter="",
            random_delimiters=separators,
            valid_delimiters=self.delimiters_full,
        )
        if prefixes == separators:
            return pwd
        elif separators and not prefixes:
            return pwd[1:-1]
        elif prefixes and not separators:
            return f"{choice(self.delimiters_full)}{pwd}{choice(self.delimiters_full)}"
