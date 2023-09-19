from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Зарегистрированные пользователи',
    callback_data='get_registered_users')
admin_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Запросы КП',
    callback_data='get_price_users')
admin_button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Список заказов',
    callback_data='get_orders')
admin_button_4: InlineKeyboardButton = InlineKeyboardButton(
    text='Закрыть заказ',
    callback_data='finish_order'
)

admin_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[admin_button_1], [admin_button_2], [admin_button_3],
                     [admin_button_4]])

