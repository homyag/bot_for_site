import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from FSM.user_states_for_price import storage
from database.connect import create_async_engine_db, async_connection_db

from config_data.config import Config, load_config
from handlers import user_handlers, products_handlers, \
    notification_handlers, admins_handlers, fsm_handlers, cart_handler, \
    admins_fsm_handlers
from main_menu.main_menu_button import set_main_menu

from middlewares import SessionMiddleware, RegisteredMiddleware

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main(configfile):
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config(configfile)

    # -> SQLAlchemy
    db_session = await async_connection_db(
        engine=await create_async_engine_db(
            config=config.db,
            echo=config.settings.sqlalchemy_echo,
        ),
        expire_on_commit=config.settings.sqlalchemy_expire_on_commit,
    )

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode=config.settings.default_parse_mode)
    dp: Dispatcher = Dispatcher(storage=storage)

    # -> Middlewares
    dp.update.middleware(SessionMiddleware(sessionmaker=db_session))
    dp.update.middleware(RegisteredMiddleware())

    # Регистриуем роутеры в диспетчере
    dp.include_router(admins_handlers.router)
    dp.include_router(admins_fsm_handlers.router)
    dp.include_router(cart_handler.router)
    dp.include_router(user_handlers.router)
    dp.include_router(products_handlers.router)
    dp.include_router(notification_handlers.router)
    dp.include_router(fsm_handlers.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    await set_main_menu(bot)
    # Запускаем поллинг
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    configfile = os.environ.get("CONFIG", "bot.ini")

    try:
        asyncio.run(main(configfile))
    except (KeyboardInterrupt, SystemError):
        print("-> Bot stopped!")
