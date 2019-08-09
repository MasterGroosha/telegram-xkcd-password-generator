# -*- coding: utf-8 -*-

en_text_help = "<a href=\"http://imgs.xkcd.com/comics/password_strength.png\">&#8203;</a>" \
    "The idea of this bot came from <a href=\"http://xkcd.com/936/\">XKCD 936</a> strip. So I decided to make " \
    "a bot which will help me quickly generate strong and readable passwords without having me open " \
    "KeePass or any other app.\n\n" \
    "You can choose from one of presets or customize passwords with /settings command and then generate them "\
    "with /generate\n\n" \
    "<b>Available presets</b>:\n" \
    "/generate_weak – 2 words, no separators between words\n"\
    "/generate_normal – 3 words, no separators between words, second word is CAPITALIZED\n"\
    "/generate_strong – 3 words, random CAPITALIZATION, random number as separator between words\n"\
    "/generate_stronger – Same as \"strong\", but using 4 words\n"\
    "/generate_insane – 4 words, second one CAPITALIZED, separators, prefixes and suffixes\n\n"\
    "By the way, this bot has its source code open: "\
    "<a href=\"https://github.com/MasterGroosha/telegram-xkcd-password-generator\">(Github)</a>\n" \
    "If you still have some questions, feel free to contact me via my bot: @msg_proxy_bot (please, don't use " \
    "it for spam)"

en_text_start = "<a href=\"http://imgs.xkcd.com/comics/password_strength.png\">&#8203;</a>" \
    "You can use this bot to generate <a href=\"http://xkcd.com/936/\">readable passwords</a>.\n" \
    "Press \"[ / ]\" to choose from presets of different strength or use /generate command to send " \
    "custom password (configurable in /settings)\n\n"\
    "If you would like to see the source code or get help, simply press /help.\n"

en_text_settings_choose = "Here are your current settings:\n" \
    "*Number of words*: {num_of_words!s}\n" \
    "*Extra prefixes/suffixes*: {prefixes}\n" \
    "*Separators between words*: {separators}\n\n" \
    "You can edit these settings using buttons below.\n"\
    "After you're satisfied with results, use /generate command"

ru_text_help = "<a href=\"http://imgs.xkcd.com/comics/password_strength.png\">&#8203;</a>" \
    "Идея по созданию этого бота пришла ко мне после прочтения комикса <a href=\"http://xkcd.com/936/\">XKCD 936</a>. " \
    "После чего я решил создать инструмент для удобной генерации сложных, но читабельных паролей без необходимости " \
    "открывать KeePass или что-либо ещё.\n\n" \
    "Вы можете выбрать один из шаблонов для генерации пароля или настроить его по своему желанию командой /settings. "\
    "Затем создайте пароль командой /generate\n\n" \
    "<b>Доступные шаблоны</b>:\n" \
    "/generate_weak – 2 слова, без разделителей\n"\
    "/generate_normal – 3 слова, без разделителей между словами, второе слово написано ПРОПИСНЫМИ буквами\n"\
    "/generate_strong – 3 слова, случайный выбор слова для записи ПРОПИСНЫМИ, случайная цифра в качестве разделителя\n"\
    "/generate_stronger – То же, что и предыдущее, но используются 4 слова\n"\
    "/generate_insane – 4 слова, второе ПРОПИСНЫМИ буквами, есть разделители, префиксы и суффиксы\n\n"\
    "Между прочим, исходный код бота открыт: "\
    "<a href=\"https://github.com/MasterGroosha/telegram-xkcd-password-generator\">(Github)</a>\n" \
    "Если у вас остались какие-либо вопросы, можете задать их через бота @msg_proxy_bot (пожалуйста, " \
    "не спамьте!)"

ru_text_start = "<a href=\"http://imgs.xkcd.com/comics/password_strength.png\">&#8203;</a>" \
    "Вы можете использовать этого бота для генерации безопасных <a href=\"http://xkcd.com/936/\">читабельных паролей</a>.\n" \
    "Нажмите \"[ / ]\" для создания пароля по одному из готовых шаблонов разной степени сложности или отправьте" \
    "/generate для создания произвольного пароля (сложность настраивается в настройках: /settings)\n\n" \
    "Если вам интересны исходники бота или есть какие-то вопросы, отправьте /help.\n"

ru_text_settings_choose = "Ваши настройки:\n" \
    "*Количество слов*: {num_of_words!s}\n" \
    "*Префиксы/суффиксы*: {prefixes}\n" \
    "*Разделители между словами*: {separators}\n\n" \
    "Используйте кнопки ниже для изменения настроек.\n"\
    "Затем используйте команду /generate для генерации пароля с этими настройками."

strings = {
    "en": {
        "start": en_text_start,
        "help": en_text_help,
        "settings": en_text_settings_choose,
        "plusword": "+ word",
        "minusword": "- word",
        "pluspref": "Add prefixes",
        "minuspref": "Remove prefixes",
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
        "pluspref": "Добавить префиксы",
        "minuspref": "Убрать префиксы",
        "plussep": "Добавить разделители",
        "minussep": "Убрать разделители",
        "regenerate": "🔄 Новый пароль",
        "no": "Нет",
        "yes": "Да"
    }
}
