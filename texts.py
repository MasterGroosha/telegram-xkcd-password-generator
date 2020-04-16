en_text_help = """<a href="http://imgs.xkcd.com/comics/password_strength.png">&#8203;</a>\
The idea of this bot came from <a href="http://xkcd.com/936/">XKCD 936</a> strip. So I decided to make \
a bot which will help me quickly generate strong and readable passwords without having me open " \
KeePass or any other app.

You can choose from one of presets or customize passwords with /settings command and then generate them with /generate.

<b>Available presets</b>:
/generate_weak – 2 words, no separators between words
/generate_normal – 3 words, no separators between words, second word is CAPITALIZED
/generate_strong – 3 words, random CAPITALIZATION, random number as separator between words
/generate_stronger – Same as "strong", but using 4 words
/generate_insane – 4 words, second one CAPITALIZED, separators, prefixes and suffixes

By the way, check out bot's source code: \
<a href="https://github.com/MasterGroosha/telegram-xkcd-password-generator">Github</a>"""

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

Вы можете выбрать один из шаблонов для генерации пароля или настроить его по своему желанию командой /settings. \
Затем создайте пароль командой /generate.

<b>Доступные шаблоны</b>:
/generate_weak – 2 слова, без разделителей
/generate_normal – 3 слова, без разделителей между словами, второе слово написано ПРОПИСНЫМИ буквами
/generate_strong – 3 слова, случайный выбор слова для записи ПРОПИСНЫМИ, случайная цифра в качестве разделителя
/generate_stronger – То же, что и предыдущее, но используются 4 слова
/generate_insane – 4 слова, второе ПРОПИСНЫМИ буквами, есть разделители, префиксы и суффиксы

Исходные тексты бота доступны по ссылке: \
<a href="https://github.com/MasterGroosha/telegram-xkcd-password-generator">Github</a>"""

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

strings = {
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
