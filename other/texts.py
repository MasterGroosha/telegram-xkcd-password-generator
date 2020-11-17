from collections import defaultdict
from typing import Dict


def get_settings_string(user_data: Dict, user_language: str) -> str:
    toggles = ["no", "yes"]  # Choose from "no" or "yes" key depending on False/True values
    return all_strings.get(user_language, "en")["settings"].format(
        num_of_words=user_data["words_count"],
        prefixes=all_strings[user_language][toggles[bool(user_data["prefixes_suffixes"])]],
        separators=all_strings[user_language][toggles[bool(user_data["separators"])]]
    )


def get_language(lang_code):
    langs = defaultdict(lambda: 'en', {'ru': 'ru'})
    return langs[lang_code.split("-")[0]] if lang_code else 'en'


en_text_help = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
The idea of this bot came from <a href="http://xkcd.com/936/">XKCD 936</a> strip. So I decided to make \
a bot which will help me quickly generate strong and readable passwords without having me open " \
KeePass or any other app.

Choose from one of presets or customize passwords with /settings command and then generate them with /generate.
You can also use this bot in <a href="https://core.telegram.org/bots/inline">inline mode</a>.

<b>Available presets</b>:
/generate_weak – 2 words, no digits
/generate_normal – 3 words, random UPPERCASE, separated by numbers
/generate_strong – 4 words, random UPPERCASE, no separators
/generate_insane – 3 words, prefixes, suffixes, separators, random UPPERCASE

By the way, check out bot's source code: \
<a href="https://git.groosha.space/groosha/passgenbot">GitLab</a> or 
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

Выберите один из шаблонов для генерации пароля или настроить по своему желанию командой /settings. \
Затем создайте пароль командой /generate.
Также поддерживается работа в <a href="https://core.telegram.org/bots/inline">инлайн-режиме</a>.

<b>Доступные шаблоны</b>:
/generate_weak – 2 слова строчными буквами, без разделителей
/generate_normal – 3 слова, случайных выбор ПРОПИСНЫХ слов, случайные цифры в качестве разделителей
/generate_strong – 4 слова, случайных выбор ПРОПИСНЫХ слов, без разделителей
/generate_insane – 3 слова, случайных выбор ПРОПИСНЫХ слов, есть разделители, префиксы и суффиксы

Исходные тексты бота доступны по ссылке: \
<a href="https://git.groosha.space/groosha/passgenbot">GitLab</a> или 
<a href="https://github.com/MasterGroosha/telegram-xkcd-password-generator">GitHub</a> (зеркало)."""

ru_text_start = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
Вы можете использовать этого бота для генерации безопасных <a href="http://xkcd.com/936/">читабельных паролей</a>.
Нажмите "[ / ]" для создания пароля по одному из готовых шаблонов разной степени сложности или отправьте \
/generate для создания произвольного пароля (сложность настраивается в настройках: /settings).

Если вам интересны исходники бота или есть какие-то вопросы, отправьте /help."""

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
        "yes": "Yes"
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
        "yes": "Да"
    }
}
