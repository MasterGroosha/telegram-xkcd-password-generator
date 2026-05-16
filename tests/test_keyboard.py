import pytest

from bot.callback_factories import GenerateCallback
from bot.handlers.generate import build_xkcd_keyboard

PASSWORD = "testpassword"


def _actions(row: list) -> list[str]:
    return [GenerateCallback.unpack(btn.callback_data).action for btn in row if btn.callback_data]


def _base_params(**overrides) -> dict:
    params = {"type": "normal", "word_count": 3, "delimiters": True, "edge_delimiters": False}
    params.update(overrides)
    return params


# --- word count row ---

def test_word_count_2_shows_only_plus():
    kb = build_xkcd_keyboard(_base_params(word_count=2), PASSWORD, "en")
    row = kb.inline_keyboard[0]
    actions = _actions(row)
    assert "word_plus" in actions
    assert "word_minus" not in actions
    assert len(row) == 1


def test_word_count_5_shows_only_minus():
    kb = build_xkcd_keyboard(_base_params(word_count=5), PASSWORD, "en")
    row = kb.inline_keyboard[0]
    actions = _actions(row)
    assert "word_minus" in actions
    assert "word_plus" not in actions
    assert len(row) == 1


@pytest.mark.parametrize("word_count", [3, 4])
def test_word_count_mid_shows_both(word_count: int):
    kb = build_xkcd_keyboard(_base_params(word_count=word_count), PASSWORD, "en")
    row = kb.inline_keyboard[0]
    actions = _actions(row)
    assert "word_minus" in actions
    assert "word_plus" in actions
    assert len(row) == 2


# --- delimiters row ---

def test_delimiters_row_action():
    kb = build_xkcd_keyboard(_base_params(), PASSWORD, "en")
    row = kb.inline_keyboard[1]
    assert _actions(row) == ["toggle_delimiters"]


# --- edge delimiters row ---

def test_edge_row_action():
    kb = build_xkcd_keyboard(_base_params(), PASSWORD, "en")
    row = kb.inline_keyboard[2]
    assert _actions(row) == ["toggle_edge"]


# --- regenerate row ---

def test_regenerate_row_action():
    kb = build_xkcd_keyboard(_base_params(), PASSWORD, "en")
    row = kb.inline_keyboard[3]
    assert _actions(row) == ["regenerate"]


# --- copy password row ---

def test_copy_password_row_has_no_callback():
    kb = build_xkcd_keyboard(_base_params(), PASSWORD, "en")
    row = kb.inline_keyboard[4]
    assert len(row) == 1
    btn = row[0]
    assert btn.callback_data is None
    assert btn.copy_text is not None
    assert btn.copy_text.text == PASSWORD


# --- total row count ---

@pytest.mark.parametrize("word_count,expected_rows", [(2, 6), (3, 6), (5, 6)])
def test_total_row_count(word_count: int, expected_rows: int):
    kb = build_xkcd_keyboard(_base_params(word_count=word_count), PASSWORD, "en")
    assert len(kb.inline_keyboard) == expected_rows


def test_delete_row_action_and_style():
    kb = build_xkcd_keyboard(_base_params(), PASSWORD, "en")
    row = kb.inline_keyboard[5]
    assert len(row) == 1
    btn = row[0]
    assert GenerateCallback.unpack(btn.callback_data).action == "delete"
    assert btn.style == "danger"
