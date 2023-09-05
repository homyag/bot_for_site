from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# песок

alluvial_sand: InlineKeyboardButton = InlineKeyboardButton(
    text="Песок намывной - 1800 рублей за тонну",
    callback_data='alluvial_sand'
)

quarry_sand: InlineKeyboardButton = InlineKeyboardButton(
    text="Песок карьерный - 1950 рублей за тонну",
    callback_data='quarry_sand'
)

crushing_sand: InlineKeyboardButton = InlineKeyboardButton(
    text="Песок из отсева дробления - 1250 рублей за тонну",
    callback_data='crushing_sand'
)

back_to_non_metallic_materials: InlineKeyboardButton = InlineKeyboardButton(
    text="назад к категориям",
    callback_data='non_metallic_materials'
)

markup_sand: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[alluvial_sand],
                     [quarry_sand],
                     [crushing_sand],
                     [back_to_non_metallic_materials]],

)