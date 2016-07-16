#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO: Make CAPITALIZATION configurable

import telebot
from telebot import types
import config
import cherrypy
from xkcdpass import xkcd_password as xp
import random
import texts
import dbworker
import botan

bot = telebot.TeleBot(config.token)


def make_settings_keyboard_for_user(user_id):
    """
    Prepare keyboard for user based on his settings

    :param user_id: User ID in Telegram
    :return: Inline Keyboard object
    """
    user = dbworker.get_person(user_id)
    kb = types.InlineKeyboardMarkup()

    wrds_lst = []
    if user["word_count"] >= (config.length_min + 1):
        wrds_lst.append(types.InlineKeyboardButton(text="– word", callback_data="minus_word"))
    if user["word_count"] <= (config.length_max - 1):
        wrds_lst.append(types.InlineKeyboardButton(text="+ word", callback_data="plus_word"))
    kb.add(*wrds_lst)

    if user["prefixes"]:
        kb.add(types.InlineKeyboardButton(text="Remove prefixes", callback_data="disable_prefixes"))
    else:
        kb.add(types.InlineKeyboardButton(text="Add prefixes", callback_data="enable_prefixes"))

    if user["separators"]:
        kb.add(types.InlineKeyboardButton(text="Remove separators", callback_data="disable_separators"))
    else:
        kb.add(types.InlineKeyboardButton(text="Add separators", callback_data="enable_separators"))

    return kb


# In case you have HUGE problems, uncomment these lines and let bot to skip all "bad" messages
# @bot.message_handler(func=lambda message: True)
# def skip(message):
#     return


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, texts.text_start, parse_mode="HTML")
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Start')
    return


@bot.message_handler(commands=["help"])
def cmd_help(message):
    bot.send_message(message.chat.id, texts.text_help, parse_mode="HTML")
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Help')
    return


@bot.message_handler(commands=["settings"])
def cmd_settings(message):
    bot.send_message(message.chat.id, text=dbworker.get_settings_text(message.chat.id),
                     reply_markup=make_settings_keyboard_for_user(message.chat.id), parse_mode="Markdown")
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Settings')
    return


# Used to decide whether to capitalize the whole world or not
def throw_random():
    return random.randint(0, 1)


def generate_weak_pwd():
    # 2 words, no separators between words
    return xp.generate_xkcdpassword(wordlist=wordlist, numwords=2, delimiter="")


def generate_normal_pwd():
    # 3 words, no separators between words, second word is CAPITALIZED
    words = xp.generate_xkcdpassword(wordlist=wordlist, numwords=3, delimiter=" ").split()
    return "{0}{1}{2}".format(words[0], str.upper(words[1]), words[2])


def generate_strong_pwd():
    # 3 words, random CAPITALIZATION, random number as separator between words
    words = xp.generate_xkcdpassword(wordlist=wordlist, numwords=3, delimiter=" ").split()
    return "{word0}{randnum0}{word1}{randnum1}{word2}".format(word0=str.upper(words[0]) if throw_random() else words[0],
                                                              word1=str.upper(words[1]) if throw_random() else words[1],
                                                              word2=str.upper(words[2]) if throw_random() else words[2],
                                                              randnum0=random.randint(0, 9),
                                                              randnum1=random.randint(0, 9))


def generate_stronger_pwd():
    # Same as "strong", but using 4 words
    words = xp.generate_xkcdpassword(wordlist=wordlist, numwords=4, delimiter=" ").split()
    return "{word0}{randnum0}{word1}{randnum1}{word2}{randnum2}{word3}" \
        .format(word0=str.upper(words[0]) if throw_random() else words[0],
                word1=str.upper(words[1]) if throw_random() else words[1],
                word2=str.upper(words[2]) if throw_random() else words[2],
                word3=str.upper(words[3]) if throw_random() else words[3],
                randnum0=random.randint(0, 9),
                randnum1=random.randint(0, 9),
                randnum2=random.randint(0, 9))


def generate_insane_pwd():
    # 4 words, second one CAPITALIZED, separators, prefixes and suffixes
    words = xp.generate_xkcdpassword(wordlist=wordlist, numwords=4, delimiter=" ").split()
    return "{randsymbol}{randsymbol}{word0}{separator}{word1}{separator}{word2}{randsymbol}{randsymbol}" \
        .format(randsymbol=random.choice("!$%^&*-_+=:|~?/.;0123456789"),
                word0=words[0],
                word1=str.upper(words[1]),
                word2=words[2],
                separator=random.choice(".$*;_=:|~?!%-+"))


@bot.message_handler(commands=["generate"])
def generate_custom(message):
    user = dbworker.get_person(message.chat.id)
    words = [str.upper(word) if throw_random() else word for word in xp.generate_xkcdpassword(
        wordlist=wordlist, numwords=user["word_count"], delimiter=" ").split()
             ]
    # Generate password without prefixes & suffixes
    _pwd = random.choice(".$*;_=:|~?!%-+").join(words) if user["separators"] else "".join(words)

    # Add prefixes/suffixes (if needed)
    if user["prefixes"]:
        password = "{prefix!s}{password}{prefix!s}".format(
            prefix=random.choice("!$%^&*-_+=:|~?/.;0123456789"),
            password=_pwd
        )
    else:
        password = _pwd

    bot.send_message(message.chat.id, password)
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Custom password')
    return


@bot.message_handler(commands=["generate_weak"])
def cmd_generate_weak_password(message):
    bot.send_message(message.chat.id, generate_weak_pwd())
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Weak password')
    return


@bot.message_handler(commands=["generate_normal"])
def cmd_generate_normal_password(message):
    bot.send_message(message.chat.id, text=generate_normal_pwd())
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Normal password')
    return


@bot.message_handler(commands=["generate_strong"])
def generate_normal_password(message):
    bot.send_message(message.chat.id, text=generate_strong_pwd())
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Strong password')
    return


@bot.message_handler(commands=["generate_stronger"])
def cmd_generate_normal_password(message):
    bot.send_message(message.chat.id, text=generate_stronger_pwd())
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Stronger password')
    return


@bot.message_handler(commands=["generate_insane"])
def cmd_generate_normal_password(message):
    bot.send_message(message.chat.id, text=generate_insane_pwd())
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Insane password')
    return


@bot.message_handler(func=lambda message: True)
def default(message):
    bot.send_message(message.chat.id, text=generate_strong_pwd())
    if config.botan_id:
        botan.track(config.botan_id, message.chat.id, message, 'Strong password (by rand message)')
    return


@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    if call.data == "disable_prefixes":
        dbworker.change_prefixes(call.from_user.id, enable_prefixes=False)
    if call.data == "enable_prefixes":
        dbworker.change_prefixes(call.from_user.id, enable_prefixes=True)
    if call.data == "disable_separators":
        dbworker.change_separators(call.from_user.id, enable_separators=False)
    if call.data == "enable_separators":
        dbworker.change_separators(call.from_user.id, enable_separators=True)
    if call.data == "minus_word":
        dbworker.change_word_count(call.from_user.id, increase=False)
    if call.data == "plus_word":
        dbworker.change_word_count(call.from_user.id, increase=True)
    bot.edit_message_text(text=dbworker.get_settings_text(call.from_user.id), chat_id=call.from_user.id,
                          message_id=call.message.message_id, parse_mode="Markdown")
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                  reply_markup=make_settings_keyboard_for_user(call.from_user.id))


@bot.inline_handler(lambda query: True)
def inline(query):
    results = [
        types.InlineQueryResultArticle(
            id="1",
            title="Insane password",
            description="2 prefixes, 2 suffixes, 3 words, separated by the same (random) symbol",
            input_message_content=types.InputTextMessageContent(
                message_text=generate_insane_pwd()
            ),
            thumb_url="https://raw.githubusercontent.com/Kondra007/telegram-xkcd-password-generator/master/img/pwd_green.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="2",
            title="Very strong password",
            description="4 words, random uppercase, separated by numbers",
            input_message_content=types.InputTextMessageContent(
                message_text=generate_stronger_pwd()
            ),
            thumb_url="https://raw.githubusercontent.com/Kondra007/telegram-xkcd-password-generator/master/img/pwd_green.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="3",
            title="Strong password",
            description="3 words, random uppercase, separated by numbers",
            input_message_content=types.InputTextMessageContent(
                message_text=generate_strong_pwd()
            ),
            thumb_url="https://raw.githubusercontent.com/Kondra007/telegram-xkcd-password-generator/master/img/pwd_yellow.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="4",
            title="Normal password",
            description="3 words, second one is uppercase",
            input_message_content=types.InputTextMessageContent(
                message_text=generate_normal_pwd()
            ),
            thumb_url="https://raw.githubusercontent.com/Kondra007/telegram-xkcd-password-generator/master/img/pwd_yellow.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="5",
            title="Weak password",
            description="2 words, no digits",
            input_message_content=types.InputTextMessageContent(
                message_text=generate_weak_pwd()
            ),
            thumb_url="https://raw.githubusercontent.com/Kondra007/telegram-xkcd-password-generator/master/img/pwd_red.png",
            thumb_height=64,
            thumb_width=64,
        )
    ]
    bot.answer_inline_query(inline_query_id=query.id, results=results, cache_time=1, is_personal=True)
    if config.botan_id:
        botan.track(config.botan_id, -1, {}, 'Inline Mode')
    return


class WebhookServer(object):
    """
    This is my custom CherryPyServer Object for use with Nginx backend.
    You may want to get original WebhookServer object here: http://bit.ly/29ETlEy
    """
    @cherrypy.expose
    def index(self):
        length = int(cherrypy.request.headers['content-length'])
        json_string = cherrypy.request.body.read(length).decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''


if __name__ == '__main__':
    global wordlist
    wordlist = xp.generate_wordlist(wordfile=config.words_file, min_length=4, max_length=10, valid_chars="[a-z]")

    # You may want to use webhooks here...
    bot.polling(none_stop=True)

