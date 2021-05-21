from collections import defaultdict


def get_language(lang_code) -> str:
    """
    Returns language code from {langs} dict or "en" as fallback value

    :param lang_code: language code taken from Message object
    :return: language code from {langs} dict or "en" as fallback value
    """
    langs = defaultdict(lambda: "en", {"ru": "ru"})
    return langs[lang_code.split("-")[0]] if lang_code else "en"


def get_string(lang_code: str, string_id: str) -> str:
    """
    Returns string from {all_strings} dictionary based on user's language code

    :param lang_code: language code taken from Message object
    :param string_id: ID of string to return
    :return: requested string by lang_code and ID
    """
    lang = get_language(lang_code)
    try:
        return all_strings[lang][string_id]
    except KeyError:
        # TODO: log this error
        return "ERR_NO_STRING"


def get_settings_string(lang_code: str, words_count: int, separators_enabled: bool, prefixes_enabled: bool) -> str:
    """
    Returns text of user's current settings

    :param lang_code: language code taken from Message object
    :param words_count: number of words in custom password
    :param separators_enabled: whether separators between words are enabled
    :param prefixes_enabled: whether password should be enclosed in one extra delimiter
    :return: text of user's current settings
    """
    toggles = ["no", "yes"]  # Choose between "no" and "yes" key depending on False/True values
    lang = get_language(lang_code)
    separators_string = get_string(lang, toggles[separators_enabled])
    prefixes_string = get_string(lang, toggles[prefixes_enabled])
    return get_string(lang, "settings").format(
        num_of_words=words_count,
        prefixes=prefixes_string,
        separators=separators_string
    )



en_text_help = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
The idea of this bot came from <a href="http://xkcd.com/936/">XKCD 936</a> strip. So I decided to make \
a bot which will help me quickly generate strong and readable passwords without having me open " \
KeePass or any other app.

Choose from one of presets or customize passwords with /settings command and then generate them with /generate.
You can also use this bot in <a href="https://core.telegram.org/bots/inline">inline mode</a>.

<b>Available presets</b>:
/generate_weak – 2 words, no digits or separators
/generate_normal – 3 words, random UPPERCASE, separated by numbers
/generate_strong – 4 words, random UPPERCASE, separated by numbers or special characters

By the way, check out bot's source code: \
<a href="https://git.groosha.space/shared/passgenbot">GitLab</a> or 
<a href="https://github.com/MasterGroosha/telegram-xkcd-password-generator">GitHub</a> (mirror)."""

en_text_start = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
You can use this bot to generate <a href="http://xkcd.com/936/">readable passwords</a>.
Press "[ / ]" to choose from presets of different strength or use /generate command to send " \
custom password (configurable in /settings)

If you would like to see the source code or get help, simply press /help."""

en_text_settings_choose = """Here are your current settings:
<b>Number of words</b>: {num_of_words!s}
<b>Extra prefixes/suffixes</b>: {prefixes}
<b>Separators between words</b>: {separators}

You can edit these settings using buttons below.
After you're satisfied with results, use /generate command"""

ru_text_help = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
Идея по созданию этого бота пришла ко мне после прочтения комикса <a href="http://xkcd.com/936/">XKCD 936</a>. \
После чего я решил создать инструмент для удобной генерации сложных, но читабельных паролей без необходимости \
открывать KeePass или что-либо ещё.

Выберите один из шаблонов для генерации пароля или настройте его по своему желанию командой /settings. \
Затем создайте пароль командой /generate.
Также поддерживается работа в <a href="https://core.telegram.org/bots/inline">инлайн-режиме</a>.

<b>Доступные шаблоны</b>:
/generate_weak – 2 слова строчными буквами, без разделителей
/generate_normal – 3 слова, случайных выбор ПРОПИСНЫХ слов, случайные цифры в качестве разделителей
/generate_strong – 4 слова, случайных выбор ПРОПИСНЫХ слов, цифры и спецсимволы в качестве разделителей

Исходные тексты бота доступны по ссылке: \
<a href="https://git.groosha.space/shared/passgenbot">GitLab</a> или 
<a href="https://github.com/MasterGroosha/telegram-xkcd-password-generator">GitHub</a> (зеркало)."""

ru_text_start = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
Вы можете использовать этого бота для генерации безопасных <a href="http://xkcd.com/936/">читабельных паролей</a>.
Нажмите "[ / ]" для создания пароля по одному из готовых шаблонов разной степени сложности или отправьте \
/generate для создания произвольного пароля (сложность настраивается в настройках: /settings).

Справка и исходники – /help."""

ru_text_settings_choose = """Ваши настройки:
<b>Количество слов</b>: {num_of_words!s}
<b>Префиксы/суффиксы</b>: {prefixes}
<b>Разделители между словами</b>: {separators}

Используйте кнопки ниже для изменения настроек.
Затем вызовите команду /generate для генерации пароля с этими настройками."""

all_strings = {
    "en": {
        "start": en_text_start,
        "help": en_text_help,
        "settings": en_text_settings_choose,
        "plusword": "+ word",
        "minusword": "- word",
        "pluspref": "Add prefix & suffix",
        "minuspref": "Remove prefix & suffix",
        "plussep": "Add separators",
        "minussep": "Remove separators",
        "regenerate": "🔄 Regenerate",
        "no": "No",
        "yes": "Yes",
        "inline_weak_title": "Weak password",
        "inline_weak_description": "2 words, no digits or separators",
        "inline_normal_title": "Normal password",
        "inline_normal_description": "3 words, random UPPERCASE, separated by numbers",
        "inline_strong_title": "Strong password",
        "inline_strong_description": "4 words, random UPPERCASE, separated by numbers or special characters"
    },
    "ru": {
        "start": ru_text_start,
        "help": ru_text_help,
        "settings": ru_text_settings_choose,
        "plusword": "+ слово",
        "minusword": "- слово",
        "pluspref": "Добавить префикс и суффикс",
        "minuspref": "Убрать префикс и суффикс",
        "plussep": "Добавить разделители",
        "minussep": "Убрать разделители",
        "regenerate": "🔄 Новый пароль",
        "no": "Нет",
        "yes": "Да",
        "inline_weak_title": "Слабый пароль",
        "inline_weak_description": "2 слова строчными буквами, без разделителей",
        "inline_normal_title": "Средний пароль",
        "inline_normal_description": "3 слова, случайных выбор ПРОПИСНЫХ слов, случайные цифры в качестве разделителей",
        "inline_strong_title": "Надёжный пароль",
        "inline_strong_description": "4 слова, случайных выбор ПРОПИСНЫХ слов, цифры и спецсимволы в качестве разделителей"
    }
}
