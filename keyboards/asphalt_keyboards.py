from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.subcategory_keyboard import back_button

# асфальт

asphalt: InlineKeyboardButton = InlineKeyboardButton(
    text="Асфальтобетон - 8000 рублей/тонна",
    callback_data='asphalt'
)


markup_asphalt: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[asphalt],
                     [back_button]],

)