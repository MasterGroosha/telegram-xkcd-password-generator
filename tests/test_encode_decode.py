import pytest

from bot.handlers.generate import decode, encode

SAMPLE_PAYLOAD = {
    "type": "normal",
    "word_count": 3,
    "delimiters": True,
    "edge_delimiters": False,
}


def test_encode_returns_html_anchor():
    result = encode(SAMPLE_PAYLOAD)
    assert result.startswith('<a href="http://127.0.0.1/?d=')
    assert result.endswith('</a>')


def test_encode_contains_zero_width_space():
    result = encode(SAMPLE_PAYLOAD)
    assert "​" in result


def test_decode_from_url():
    url = "http://127.0.0.1/?d=eyJ0eXBlIjoibm9ybWFsIiwid29yZF9jb3VudCI6MywiZGVsaW1pdGVycyI6dHJ1ZSwiZWRnZV9kZWxpbWl0ZXJzIjpmYWxzZX0"
    result = decode(url)
    assert result == SAMPLE_PAYLOAD


def test_roundtrip():
    html_anchor = encode(SAMPLE_PAYLOAD)
    result = decode(html_anchor)
    assert result == SAMPLE_PAYLOAD


@pytest.mark.parametrize("payload", [
    {"type": "normal", "word_count": 2, "delimiters": False, "edge_delimiters": False},
    {"type": "normal", "word_count": 5, "delimiters": True, "edge_delimiters": True},
    {"type": "acrostic", "word_count": 4, "delimiters": False, "edge_delimiters": True},
])
def test_roundtrip_various_payloads(payload: dict):
    assert decode(encode(payload)) == payload


def test_decode_no_url_returns_none():
    assert decode("no url here") is None


def test_decode_wrong_host_returns_none():
    assert decode("http://example.com/?d=eyJmb28iOiJiYXIifQ") is None


def test_decode_invalid_base64_returns_none():
    assert decode("http://127.0.0.1/?d=!!!invalid!!!") is None


def test_decode_invalid_json_returns_none():
    import base64
    bad = base64.urlsafe_b64encode(b"not json").decode().rstrip("=")
    assert decode(f"http://127.0.0.1/?d={bad}") is None
