from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.concrete_keyboards import back_to_sub_button

# кладочный раствор

masonry_М50ПК3: InlineKeyboardButton = InlineKeyboardButton(
    text="артикул М50ПК3 - 8500 рублей/м3",
    callback_data='М50ПК3'
)

masonry_М75ПК3: InlineKeyboardButton = InlineKeyboardButton(
    text="артикул М75ПК3 - 9000 рублей/м3",
    callback_data='М75ПК3'
)

masonry_М100ПК3: InlineKeyboardButton = InlineKeyboardButton(
    text="артикул М100ПК3 - 9500 рублей/м3",
    callback_data='М100ПК3'
)

markup_masonry: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[masonry_М50ПК3],
                     [masonry_М75ПК3],
                     [masonry_М100ПК3],
                     [back_to_sub_button]]
)

