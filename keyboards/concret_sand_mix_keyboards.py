from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.concrete_keyboards import back_to_sub_button

# ЦПС

mix_CSM_1_2: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/2 - 10000 рублей/м3",
    callback_data='CSM_1_2'
)

mix_CSM_1_3: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/3 - 9500 рублей/м3",
    callback_data='CSM_1_3'
)

mix_CSM_1_4: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/4 - 9000 рублей/м3",
    callback_data='CSM_1_4'
)

mix_CSM_1_5: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/5 - 8500 рублей/м3",
    callback_data='CSM_1_5'
)

mix_CSM_1_6: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/6 - 8000 рублей/м3",
    callback_data='CSM_1_6'
)

mix_CSM_1_7: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/7 - 7750 рублей/м3",
    callback_data='CSM_1_7'
)

mix_CSM_1_8: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/8 - 7500 рублей/м3",
    callback_data='CSM_1_8'
)

mix_CSM_1_9: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/9 - 7250 рублей/м3",
    callback_data='CSM_1_9'
)

mix_CSM_1_10: InlineKeyboardButton = InlineKeyboardButton(
    text="ЦПС 1/10 - 7000 рублей/м3",
    callback_data='CSM_1_10'
)

markup_mix: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[mix_CSM_1_2],
                     [mix_CSM_1_3],
                     [mix_CSM_1_4],
                     [mix_CSM_1_5],
                     [mix_CSM_1_6],
                     [mix_CSM_1_7],
                     [mix_CSM_1_8],
                     [mix_CSM_1_9],
                     [mix_CSM_1_10],
                     [back_to_sub_button]],

)