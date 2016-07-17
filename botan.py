# -*- coding: utf-8 -*-
# Modified for pyTelegramBotAPI (https://github.com/eternnoir/pyTelegramBotAPI/)

import requests
import json
from telebot import types
import logging

SHORTENER_URL = 'https://api.botan.io/s/'
TRACK_URL = 'https://api.botan.io/track'


def make_json(msg):
    """
    A special method for preparing stats for Botan. Use with pyTelegramBotAPI.
    Handles both Message and CallbackQuery objects.
    """
    if isinstance(msg, types.CallbackQuery):
        try:
            return json.dumps({"Stub key": 0})
        except Exception as ex:
            logging.error(
                "Exception of type {ex_type!s} in botan_s make_json (call): {ex_reason!s}".format(ex_type=type(ex),
                                                                                                  ex_reason=str(ex)))
    if isinstance(msg, types.Message):
        try:
            if msg is None:
                return None
            return json.dumps({"Stub key": 0})
        except Exception as ex:
            logging.error(
                "Exception of type {ex_type!s} in botan_s make_json (message): {ex_reason!s}".format(ex_type=type(ex),
                                                                                                     ex_reason=str(ex)))


def track(token, uid, message, name='Message'):
    try:
        r = requests.post(
            TRACK_URL,
            params={"token": token, "uid": uid, "name": name},
            data=make_json(message),
            headers={'Content-type': 'application/json'},
        )
        return r.json()
    except requests.exceptions.Timeout:
        # set up for a retry, or continue in a retry loop
        return False
    except (requests.exceptions.RequestException, ValueError) as e:
        # catastrophic error
        print(e)
        return False


def shorten_url(url, botan_token, user_id):
    """
    Shorten URL for specified user of a bot
    """
    try:
        return requests.get(SHORTENER_URL, params={
            'token': botan_token,
            'url': url,
            'user_ids': str(user_id),
        }).text
    except:
        return url