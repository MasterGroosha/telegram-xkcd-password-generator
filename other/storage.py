from aiogram.dispatcher import FSMContext
from other.config import app_config, DBKeys


async def verify_user_data(state: FSMContext):
    """
    Verify integrity of values in FSM context and add missing ones.
    Values are compared against [default] section in config file.

    :param state: current context
    """
    changes = {}
    user_data = await state.get_data()
    for item in [a.value for a in DBKeys]:
        if item not in user_data or user_data.get(item) is None:
            changes[item] = app_config.default.__getattribute__(item)
    if len(changes.keys()) > 0:
        await state.update_data(**changes)


async def change_word_count(state: FSMContext, increase):
    """
    Change word count of generated custom passwords

    :param state: current context
    :param increase: boolean flag whether word count needs to be increased or not ( = decreased )
    """
    async with state.proxy() as data:
        current_value = data.get(DBKeys.WORDS_COUNT.value)
        if increase and (current_value+1) <= app_config.pwd_words.max:
            await state.update_data({DBKeys.WORDS_COUNT.value: current_value+1})
        elif not increase and (current_value-1) >= app_config.pwd_words.min:
            await state.update_data({DBKeys.WORDS_COUNT.value: current_value-1})


async def toggle_feature(state: FSMContext, feature_name: str, new_state: bool):
    """
    Toggle a boolean feature like "prefixes/suffixes" or "separators"

    :param state: current context
    :param feature_name: name of feature to toggle
    :param new_state: new state of feature: True or False
    """
    await state.update_data({feature_name: new_state})
