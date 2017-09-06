# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query
from tinydb.operations import increment, decrement
from texts import strings
from config import db_file
from utils import get_language


DEFAULT_WORD_COUNT = 3
DEFAULT_PREFIX_SUFFIX = True
DEFAULT_SEPARATOR = True

db = TinyDB(db_file)


def get_settings_text(user_id, lang_code):
    user = get_person(user_id)
    text = strings.get(get_language(lang_code)).get("settings").format(num_of_words=user["word_count"],
        prefixes=strings.get(get_language(lang_code)).get("yes")
            if user["prefixes"] else strings.get(get_language(lang_code)).get("no"),
        separators=strings.get(get_language(lang_code)).get("yes")
            if user["separators"] else strings.get(get_language(lang_code)).get("no"))
    return text


def user_exists(user_id):
    return True if len(db.search(Query().user_id == user_id)) > 0 else False


def get_person(user_id):
    # Check if user exists
    S = Query()
    person = db.search(S.user_id == user_id)
    if len(person) is 0:
        usr = {"user_id": user_id,
               "word_count": DEFAULT_WORD_COUNT,
               "prefixes": DEFAULT_PREFIX_SUFFIX,
               "separators": DEFAULT_SEPARATOR}
        db.insert(usr)
        return usr
    return person[0]


def change_word_count(user_id, increase):
    S = Query()
    if increase:
        db.update(increment("word_count"), S.user_id == user_id)
    else:
        db.update(decrement("word_count"), S.user_id == user_id)
    return db.search(S.user_id == user_id)[0]


def change_prefixes(user_id, enable_prefixes):
    S = Query()
    if enable_prefixes:
        db.update({"prefixes": True}, S.user_id == user_id)
    else:
        db.update({"prefixes": False}, S.user_id == user_id)
    return db.search(S.user_id == user_id)[0]


def change_separators(user_id, enable_separators):
    S = Query()
    if enable_separators:
        db.update({"separators": True}, S.user_id == user_id)
    else:
        db.update({"separators": False}, S.user_id == user_id)
    return db.search(S.user_id == user_id)[0]
