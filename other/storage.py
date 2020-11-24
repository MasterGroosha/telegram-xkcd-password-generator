from aiogram.dispatcher import FSMContext
from other.config import app_config, DBKeys


async def get_data(state: FSMContext):
    """
    Get data from FSM and also initialize missing values with default values

    :param state: current context
    """
    data = await state.get_data()
    has_changes = False
    for item in [a.value for a in DBKeys]:
        if item not in data or data.get(item) is None:
            data[item] = app_config.__getattribute__(item)
            has_changes = True
    if has_changes:
        await state.update_data(**data)
    return data


async def change_word_count(state: FSMContext, increase):
    """
    Change word count of generated custom passwords

    :param state: current context
    :param increase: boolean flag whether word count needs to be increased or not ( = decreased )
    """
    data = await get_data(state)
    current_value = data.get(DBKeys.WORDS_COUNT.value)
    if increase and (current_value+1) <= app_config.max_words:
        await state.update_data({DBKeys.WORDS_COUNT.value: current_value+1})
    elif not increase and (current_value-1) >= app_config.min_words:
        await state.update_data({DBKeys.WORDS_COUNT.value: current_value-1})


async def toggle_feature(state: FSMContext, feature_name: str, new_state: bool):
    """
    Toggle a boolean feature like "prefixes/suffixes" or "separators"

    :param state: current context
    :param feature_name: name of feature to toggle
    :param new_state: new state of feature: True or False
    """
    await state.update_data({feature_name: new_state})
