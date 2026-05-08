import pytest

from bot.pwdgen import XKCDGenerator

SEPARATORS = set(XKCDGenerator.delimiters_full)
DIGITS = set(XKCDGenerator.delimiters_numbers)

# Run each randomized assertion multiple times to guard against lucky passes
ROUNDS = 20


def test_weak_is_lowercase_alpha(gen: XKCDGenerator):
    for _ in range(ROUNDS):
        pwd = gen.weak()
        assert isinstance(pwd, str)
        assert len(pwd) > 0
        assert pwd.isalpha()
        assert pwd.islower()


def test_normal_contains_digit_separator(gen: XKCDGenerator):
    for _ in range(ROUNDS):
        pwd = gen.normal()
        assert isinstance(pwd, str)
        assert any(c in DIGITS for c in pwd), f"No digit found in: {pwd!r}"


def test_strong_contains_separator(gen: XKCDGenerator):
    for _ in range(ROUNDS):
        pwd = gen.strong()
        assert isinstance(pwd, str)
        assert any(c in SEPARATORS for c in pwd), f"No separator found in: {pwd!r}"


@pytest.mark.parametrize("word_count", [2, 3, 4, 5])
def test_custom_no_sep_no_edge_is_alpha(gen: XKCDGenerator, word_count: int):
    for _ in range(ROUNDS):
        pwd = gen.custom(word_count=word_count, separators=False, prefixes=False)
        assert isinstance(pwd, str)
        assert pwd.isalpha(), f"Expected alpha-only, got: {pwd!r}"


@pytest.mark.parametrize("word_count", [2, 3, 4, 5])
def test_custom_sep_no_edge_has_separator_not_at_boundary(gen: XKCDGenerator, word_count: int):
    for _ in range(ROUNDS):
        pwd = gen.custom(word_count=word_count, separators=True, prefixes=False)
        assert any(c in SEPARATORS for c in pwd), f"No separator found in: {pwd!r}"
        assert pwd[0] not in SEPARATORS, f"Unexpected leading separator in: {pwd!r}"
        assert pwd[-1] not in SEPARATORS, f"Unexpected trailing separator in: {pwd!r}"


@pytest.mark.parametrize("word_count", [2, 3, 4, 5])
def test_custom_no_sep_edge_has_boundary_chars(gen: XKCDGenerator, word_count: int):
    for _ in range(ROUNDS):
        pwd = gen.custom(word_count=word_count, separators=False, prefixes=True)
        assert pwd[0] in SEPARATORS, f"Expected leading separator in: {pwd!r}"
        assert pwd[-1] in SEPARATORS, f"Expected trailing separator in: {pwd!r}"
        assert pwd[1:-1].isalpha(), f"Expected alpha-only middle in: {pwd!r}"


@pytest.mark.parametrize("word_count", [2, 3, 4, 5])
def test_custom_both_has_separators(gen: XKCDGenerator, word_count: int):
    for _ in range(ROUNDS):
        pwd = gen.custom(word_count=word_count, separators=True, prefixes=True)
        assert any(c in SEPARATORS for c in pwd), f"No separator found in: {pwd!r}"
