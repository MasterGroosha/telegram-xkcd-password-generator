from aiogram import types, Dispatcher
from aiogram.utils.markdown import hcode
from bot.localization import get_string


async def inline_handler(query: types.InlineQuery):
    pwd = query.bot.get("pwd")
    data = [
        {
            "title_tag": "inline_strong_title",
            "description_tag": "inline_strong_description",
            "password_func": pwd.strong,
            "thumb_color": "green"
        },
        {
            "title_tag": "inline_normal_title",
            "description_tag": "inline_normal_description",
            "password_func": pwd.normal,
            "thumb_color": "yellow"
        },
        {
            "title_tag": "inline_weak_title",
            "description_tag": "inline_weak_description",
            "password_func": pwd.weak,
            "thumb_color": "red"
        },
    ]
    results = []
    for index, item in enumerate(data):
        results.append(
            types.InlineQueryResultArticle(
                id=str(index),
                title=get_string(query.from_user.language_code, item["title_tag"]),
                description=get_string(query.from_user.language_code, item["description_tag"]),
                input_message_content=types.InputTextMessageContent(
                    message_text=hcode(item["password_func"]())
                ),
                thumb_url=f"https://raw.githubusercontent.com/MasterGroosha/"
                          f"telegram-xkcd-password-generator/master/img/pwd_{item['thumb_color']}.png",
                thumb_height=64,
                thumb_width=64,
            )
        )
    await query.answer(results, cache_time=1, is_personal=True)


def register_inline_mode(dp: Dispatcher):
    dp.register_inline_handler(inline_handler)
