# -*- coding: utf-8 -*-


def get_language(lang_code):
    return lang_code.split("-")[0] if lang_code else 'en'
