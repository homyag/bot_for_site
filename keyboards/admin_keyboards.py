from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

admin_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Получить спискок зарегистрированных '
         'пользователей',
    callback_data='get_registered_users')
admin_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Получить список пользователей, '
         'запросивших КП',
    callback_data='get_price_users')
admin_button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Получить список заказов',
    callback_data='get_orders')

admin_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[admin_button_1, admin_button_2, admin_button_3]])
