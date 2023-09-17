from aiogram import types
from config_data.config import Config, load_config

# Загрузите конфигурацию бота
config = load_config("bot.ini")


async def send_notification(bot, admin_ids, message_text):
    for admin_id in admin_ids:
        try:
            await bot.send_message(chat_id=admin_id, text=message_text)
        except Exception as e:
            # Обработка ошибок отправки сообщения, если необходимо
            print(f"Ошибка при отправке сообщения админу {admin_id}: {str(e)}")