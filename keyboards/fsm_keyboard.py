from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yes_button_for_fsm: InlineKeyboardButton = InlineKeyboardButton(
    text='да',
    callback_data='yes_i_agree_button'
)

no_button_for_fsm: InlineKeyboardButton = InlineKeyboardButton(
    text='нет',
    callback_data='no_i_didnt_agree'
)


markup_start_fsm: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[yes_button_for_fsm],
                                     [no_button_for_fsm]])
