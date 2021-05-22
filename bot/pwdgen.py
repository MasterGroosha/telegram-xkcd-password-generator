from random import choice
from xkcdpass import xkcd_password


class XKCD:
    delimiters_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    delimiters_full = ["!", "$", "%", "^", "&", "*", "-", "_", "+", "=",
                       ":", "|", "~", "?", "/", ".", ";"] + delimiters_numbers

    def __init__(self, filename: str):
        self.wordlist = xkcd_password.generate_wordlist(
            wordfile=filename, valid_chars="[a-z]", min_length=4, max_length=10,
        )

    def weak(self):
        # 2 words, no separators between words
        return xkcd_password.generate_xkcdpassword(self.wordlist, numwords=2, delimiter="", )

    def normal(self):
        # 3 words, random CAPITALIZATION, random number as separator between words
        return xkcd_password.generate_xkcdpassword(
            self.wordlist, numwords=3, case="random", random_delimiters=True, valid_delimiters=self.delimiters_numbers
        )

    def strong(self):
        # Same as normal_pwd, but 4 words
        return xkcd_password.generate_xkcdpassword(
            self.wordlist, numwords=4, case="random", random_delimiters=True, valid_delimiters=self.delimiters_full
        )

    def custom(self, count: int, separators: bool, prefixes: bool):
        """
        Custom password generation

        :param count: number of words in password
        :param separators: bool, whether words must be separated with delimiters
        :param prefixes: bool, whether there must be chars from delimiters list in front and in back
        :return: generated custom password
        """
        pwd = xkcd_password.generate_xkcdpassword(
            self.wordlist, numwords=count, case="random", delimiter="",
            random_delimiters=separators, valid_delimiters=self.delimiters_full
        )
        if prefixes == separators:
            return pwd
        elif separators and not prefixes:
            return pwd[1:-1]
        elif prefixes and not separators:
            return f"{choice(self.delimiters_full)}{pwd}{choice(self.delimiters_full)}"
