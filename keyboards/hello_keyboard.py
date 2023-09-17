from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

hello_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Номенклатура',
    callback_data='nomenclature_pressed'
)

hello_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Запросить КП',
    callback_data='price_requested'
)

hello_button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Перейти на сайт',
    url='https://betonmariupol.ru'
)

markup_hello: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[hello_button_1],
                     [hello_button_2],
                     [hello_button_3]])
