import other.configurator as configurator


if __name__ == '__main__':
    try:
        configurator.check()
    except ValueError as ex:
        exit(ex)

    # Config initialized, now we can load everything else
    from aiogram import executor
    from misc import dp
    import handlers

    executor.start_polling(dp, skip_updates=True)
