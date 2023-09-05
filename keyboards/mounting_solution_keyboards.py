from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# монтажный раствор

mounting_РМ100ПК4: InlineKeyboardButton = InlineKeyboardButton(
    text="модель РМ100ПК4 - 9500 рублей/м3",
    callback_data='РМ100ПК4'
)

mounting_РМ150ПК4: InlineKeyboardButton = InlineKeyboardButton(
    text="модель РМ150ПК4 - 10000 рублей/м3",
    callback_data='РМ150ПК4'
)

mounting_РМ200ПК4: InlineKeyboardButton = InlineKeyboardButton(
    text="модель РМ200ПК4 - 10500 рублей/м3",
    callback_data='РМ200ПК4'
)

back_to_sub_button: InlineKeyboardButton = InlineKeyboardButton(
    text="назад к категориям",
    callback_data='back_from_mounting'
)

markup_mounting: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[mounting_РМ100ПК4],
                     [mounting_РМ150ПК4],
                     [mounting_РМ200ПК4],
                     [back_to_sub_button]]
)