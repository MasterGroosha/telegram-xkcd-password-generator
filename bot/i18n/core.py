from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

LOCALES_DIR = Path(__file__).parent / "locales"
DEFAULT_LOCALE = "en"
AVAILABLE_LOCALES = ("en", "ru")

_loader = FluentResourceLoader(str(LOCALES_DIR / "{locale}"))

_l10n_cache: dict[str, FluentLocalization] = {
    locale: FluentLocalization(
        locales=[locale, DEFAULT_LOCALE],
        resource_ids=["messages.ftl"],
        resource_loader=_loader,
    )
    for locale in AVAILABLE_LOCALES
}


def resolve_locale(language_code: str | None) -> str:
    if not language_code:
        return DEFAULT_LOCALE
    return "ru" if language_code.lower().startswith("ru") else DEFAULT_LOCALE


def t(key: str, locale: str = DEFAULT_LOCALE, **kwargs: object) -> str:
    l10n = _l10n_cache.get(locale, _l10n_cache[DEFAULT_LOCALE])
    return l10n.format_value(key, kwargs)
