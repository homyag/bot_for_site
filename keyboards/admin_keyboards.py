from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

admin_button_1 = KeyboardButton(text='Получить спискок зарегистрированных '
                                     'пользователей')
admin_button_2 = KeyboardButton(text='Получить список пользователей, '
                                     'запросивших КП')
admin_button_3 = KeyboardButton(text='Получить список заказов')

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()
kb_builder.add(admin_button_1)
kb_builder.add(admin_button_2)
kb_builder.add(admin_button_3)

# Явно сообщаем билдеру сколько хотим видеть кнопок в рядах
kb_builder.adjust(1, 1, 1)

admin_keyboard = ReplyKeyboardMarkup(keyboard=[[admin_button_1,
                                                admin_button_2,
                                                admin_button_3]],
                                     width=1)