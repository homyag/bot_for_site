from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# кнопки для номенклатуры бетона
concrete_В75П3F50W2: InlineKeyboardButton = InlineKeyboardButton(
    text="марка М100 - 10000 рублей/м3",
    callback_data='В75П3F50W2'
)

concrete_В15П4F100W4: InlineKeyboardButton = InlineKeyboardButton(
    text="марка М200 - 11000 рублей/м3",
    callback_data='В15П4F100W4'
)

concrete_В20П4F100W6: InlineKeyboardButton = InlineKeyboardButton(
    text="марка М250 - 11500 рублей/м3",
    callback_data='В20П4F100W6'
)

concrete_В225П4F150W6: InlineKeyboardButton = InlineKeyboardButton(
    text="марка М300 - 12000 рублей/м3",
    callback_data='В225П4F150W6'
)

concrete_В25П4W8F150: InlineKeyboardButton = InlineKeyboardButton(
    text="марка М350 - 12500 рублей/м3",
    callback_data='В25П4W8F150'
)

concrete_В30П4W10F200: InlineKeyboardButton = InlineKeyboardButton(
    text="марка М400 - 13500 рублей/м3",
    callback_data='В30П4W10F200'
)

back_to_sub_button: InlineKeyboardButton = InlineKeyboardButton(
    text="назад к категориям",
    callback_data='building mixes'
)

markup_concrete: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[concrete_В75П3F50W2],
                     [concrete_В15П4F100W4],
                     [concrete_В20П4F100W6],
                     [concrete_В225П4F150W6],
                     [concrete_В25П4W8F150],
                     [concrete_В30П4W10F200],
                     [back_to_sub_button]]
)
