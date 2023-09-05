from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.sand_keyboards import back_to_non_metallic_materials

# щебень

crushed_granite_10_20: InlineKeyboardButton = InlineKeyboardButton(
    text="Щебень гранитный 10-20 - 2300 рублей за тонну",
    callback_data='crushed_granite_10_20'
)

crushed_granite_20_40: InlineKeyboardButton = InlineKeyboardButton(
    text="Щебень гранитный 20-40 - 2200 рублей за тонну",
    callback_data='crushed_granite_20_40'
)

crushed_granite_5_10: InlineKeyboardButton = InlineKeyboardButton(
    text="Щебень гранитный 5-10 - 2300 рублей за тонну",
    callback_data='crushed_granite_5_10'
)

markup_crushed_granite: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[crushed_granite_10_20],
                     [crushed_granite_20_40],
                     [crushed_granite_5_10],
                     [back_to_non_metallic_materials]],

)