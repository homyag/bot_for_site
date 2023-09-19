from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from DAO.data_access_object import DataAccessObject
from FSM.admin_check_orders import FSMAdminOrder, order_dict
from config_data import load_config
from database import User
from keyboards.admin_keyboards import admin_keyboard
from keyboards.fsm_keyboard import markup_start_fsm
from keyboards.hello_keyboard import markup_hello
from utils.send_notification_to_admins import send_notification

router: Router = Router()
config = load_config("bot.ini")


@router.callback_query(F.data == 'finish_order', StateFilter(default_state))
async def process_finish_order_command(callback_query: CallbackQuery,
                                       state: FSMContext):
    if callback_query.from_user.id in config.tg_bot.admin_ids:
        await callback_query.message.edit_text(text='<b>Пожалуйста, ведите '
                                                    'заказчика: ***('
                                                    'функция в '
                                                    'разработке)***</b>\n<i>Для '
                                                    'получения данных о '
                                                    'заказах нажмите кнопку '
                                                    '"Список '
                                                    'заказов".</i>\n\nДля '
                                                    'выхода из режима '
                                                    'закрытия заказа введите '
                                                    'команду '
                                                    '/end_check_order',
                                               reply_markup=admin_keyboard)
        # Устанавливаем состояние ожидания ввода имени
        await state.set_state(FSMAdminOrder.fill_product_name)
    else:
        await callback_query.message.edit_text(
            text=f"{callback_query.from_user.username}, извините, "
                 f"но вы не являетесь администратором")


@router.message(Command(commands='end_check_order'), StateFilter(
    default_state))
async def process_cancel_check_order(message: Message):
    await message.answer(text='Отменять нечего')


@router.message(Command(commands='end_check_order'), ~StateFilter(default_state))
async def process_cancel_check_order_state(message: Message, state: FSMContext):
    await message.answer(text='Вы отменили закрытие заказа.')
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()

