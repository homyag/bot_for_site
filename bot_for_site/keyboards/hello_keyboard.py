from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.callback import GoodsCallbackFactory

hello_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='номенклатура',
    callback_data='nomenclature_pressed'
)

hello_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='запросить КП',
    callback_data='price_requested'
)

markup_hello: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[hello_button_1],
                                     [hello_button_2]])
