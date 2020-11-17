from aiogram import types
from misc import dp
from other import pwdgen


@dp.inline_handler()  # Default inline mode handler
async def inline(query: types.InlineQuery):
    results = [
        types.InlineQueryResultArticle(
            id="1",
            title="Insane password",
            description="3 words, prefixes, suffixes, separators, random uppercase",
            input_message_content=types.InputTextMessageContent(
                message_text=f"<code>{pwdgen.generate_insane_pwd()}</code>"
            ),
            thumb_url="https://raw.githubusercontent.com/MasterGroosha/telegram-xkcd-password-generator/master/img/pwd_green.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="2",
            title="Strong password",
            description="4 words, random uppercase, no separators",
            input_message_content=types.InputTextMessageContent(
                message_text=f"<code>{pwdgen.generate_strong_pwd()}</code>"
            ),
            thumb_url="https://raw.githubusercontent.com/MasterGroosha/telegram-xkcd-password-generator/master/img/pwd_green.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="3",
            title="Normal password",
            description="3 words, random uppercase, separated by numbers",
            input_message_content=types.InputTextMessageContent(
                message_text=f"<code>{pwdgen.generate_normal_pwd()}</code>"
            ),
            thumb_url="https://raw.githubusercontent.com/MasterGroosha/telegram-xkcd-password-generator/master/img/pwd_yellow.png",
            thumb_height=64,
            thumb_width=64,
        ),

        types.InlineQueryResultArticle(
            id="5",
            title="Weak password",
            description="2 words, no digits",
            input_message_content=types.InputTextMessageContent(
                message_text=f"<code>{pwdgen.generate_weak_pwd()}</code>"
            ),
            thumb_url="https://raw.githubusercontent.com/MasterGroosha/telegram-xkcd-password-generator/master/img/pwd_red.png",
            thumb_height=64,
            thumb_width=64,
        )
    ]
    await query.answer(results=results, cache_time=1, is_personal=True)
