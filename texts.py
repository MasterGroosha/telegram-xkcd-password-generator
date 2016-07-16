# -*- coding: utf-8 -*-


text_help = "<a href=\"http://imgs.xkcd.com/comics/password_strength.png\">&#8203;</a>" \
    "The idea of this bot came from <a href=\"http://xkcd.com/936/\">XKCD 936</a> strip. So I decided to make " \
    "a bot which will help me quickly generate strong and readable passwords without having me open " \
    "KeePass or any other app.\n\n" \
    "You can choose from one of presets or customize passwords with /settings command and then generate them"\
    "with /generate\n\n" \
    "<b>Available presets</b>:\n" \
    "/generate_weak – 2 words, no separators between words\n"\
    "/generate_normal – 3 words, no separators between words, second word is CAPITALIZED\n"\
    "/generate_strong – 3 words, random CAPITALIZATION, random number as separator between words\n"\
    "/generate_stronger – Same as \"strong\", but using 4 words\n"\
    "/generate_insane – 4 words, second one CAPITALIZED, separators, prefixes and suffixes\n\n"\
    "By the way, this bot has its source open:"\
    "<a href=\"https://github.com/Kondra007/telegram-xkcd-password-generator\">(Github)</a>\n" \
    "<b>Please note:</b> it uses <a href=\"http://botan.io/\">Botan</a> (Yandex Appmetrica) module to " \
    "track which presets are used most often. No generated passwords are saved anywhere!\n" \
    "If you still have some questions, feel free to contact me via my bot: @msg_proxy_bot (please, don't use " \
    "it for spam)"

text_start = "<a href=\"http://imgs.xkcd.com/comics/password_strength.png\">&#8203;</a>" \
             "You can use this bot to generate <a href=\"http://xkcd.com/936/\">readable passwords</a>.\n" \
             "Press \"[ / ]\" to choose from presets of different strength or use /generate command to send " \
             "custom password (configurable in /settings)\n\n"\
             "If you would like to see the source code or get help, simply press /help."

text_settings_choose = "Here are your current settings:\n" \
                       "*Number of words*: {num_of_words!s}\n" \
                       "*Extra prefixes/suffixes*: {prefixes}\n" \
                       "*Separators between words*: {separators}\n\n" \
                       "You can edit these settings using buttons below."
