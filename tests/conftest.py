from pathlib import Path

import pytest

from bot.pwdgen import XKCDGenerator

WORDS_FILE = Path(__file__).parent.parent / "words.txt"


@pytest.fixture(scope="session")
def gen() -> XKCDGenerator:
    return XKCDGenerator(str(WORDS_FILE))
