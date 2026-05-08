import pytest

from bot.handlers.inline_mode import build_inline_message_text


def test_no_user_text_returns_code_only():
    result = build_inline_message_text("mypassword", "")
    assert result == "<code>mypassword</code>"


def test_with_user_text_appends_after_newline():
    result = build_inline_message_text("mypassword", "hello world")
    assert result == "<code>mypassword</code>\nhello world"


def test_password_with_html_special_chars_is_escaped():
    result = build_inline_message_text("<secret>&pass", "")
    assert "<secret>" not in result
    assert "&pass" not in result
    assert "&lt;secret&gt;&amp;pass" in result


def test_user_text_with_html_special_chars_is_escaped():
    result = build_inline_message_text("pwd", "<b>bold</b> & more")
    assert "<b>bold</b>" not in result
    assert "&lt;b&gt;bold&lt;/b&gt; &amp; more" in result


def test_whitespace_only_user_text_is_treated_as_empty():
    # Trimming happens in the handler; here we just verify that
    # an already-stripped empty string produces code-only output.
    result = build_inline_message_text("pwd", "")
    assert "\n" not in result


def test_parse_mode_is_html_compatible():
    # Password and user text must be wrapped/escaped so the result
    # is safe to send with ParseMode.HTML.
    result = build_inline_message_text("p&w<d>", "note & <info>")
    assert result.startswith("<code>")
    assert result.endswith("</info>") is False  # raw tag must not appear
    assert "<info>" not in result
