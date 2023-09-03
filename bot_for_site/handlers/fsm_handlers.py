from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery

from keyboards.fsm_keyboard import markup_start_fsm

router: Router = Router()


# Этот хэндлер будет срабатывать на команду /start вне состояний
# и предлагать перейти к заполнению анкеты, отправив команду /fillform
@router.callback_query(F.data == 'price_requested', StateFilter(default_state))
async def process_price_command(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text='Для отправки нами коммерческого предложения оставьте,'
             '\n пожалуйста, свои координаты. Если Вы согласны, нажмите '
             'кнопку ДА.',
        reply_markup=markup_start_fsm)