from collections import defaultdict


def get_language(lang_code):
    langs = defaultdict(lambda: 'en', {'ru': 'ru'})
    return langs[lang_code.split("-")[0]] if lang_code else 'en'
