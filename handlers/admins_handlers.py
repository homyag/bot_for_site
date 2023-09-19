from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from DAO.data_access_object import DataAccessObject
from config_data import load_config
from keyboards.admin_keyboards import admin_keyboard

router: Router = Router()
config = load_config("bot.ini")


@router.message(Command(commands=['admin']))
async def process_admin_command(message: Message):
    if message.from_user.id in config.tg_bot.admin_ids:
        await message.answer(text=f"Привет {message.from_user.full_name}. "
                                  f"Список доступных действий:",
                             reply_markup=admin_keyboard)
    else:
        await message.answer(text=f"{message.from_user.full_name}, извините, "
                                  f"но вы не являетесь администратором")


@router.callback_query(F.data == 'get_orders')
async def get_all_orders(callback_query: CallbackQuery, dao: DataAccessObject):
    if callback_query.from_user.id in config.tg_bot.admin_ids:
        orders = await dao.get_all_orders_with_user_data()
        if orders:
            grouped_orders = {}

            for order in orders:
                username = order['username']
                order_date = order['order_date']
                if username not in grouped_orders:
                    grouped_orders[username] = {}

                if order_date not in grouped_orders[username]:
                    grouped_orders[username][order_date] = []

                grouped_orders[username][order_date].append(order['name'])

            orders_text = ""
            for username, dates in grouped_orders.items():
                orders_text += f"<b>Заказчик:</b> {username}, Телефон: {orders[0]['phone']}\n"
                for order_date, products in dates.items():
                    orders_text += f"<b>Дата заказа:</b> {order_date}\n"
                    orders_text += f"<b>Заказы:</b> {', '.join(products)}\n"

            await callback_query.message.answer(f"Список заказов:\n{orders_text}")
        else:
            await callback_query.message.answer("Список заказов пуст.")
    else:
        await callback_query.message.answer(
            "У вас нет прав на выполнение этой команды.")


@router.callback_query(F.data == 'get_price_users')
async def get_asked_price_users(callback_query: CallbackQuery,
                          dao: DataAccessObject):
    if callback_query.from_user.id in config.tg_bot.admin_ids:
        users_with_contacts = await dao.get_users_with_contacts()
        if users_with_contacts:
            users_text = "\n".join([
                                       f"User: {user.username}, Email: {user.e_mail}, Phone: {user.phone}"
                                       for user in users_with_contacts])
            await callback_query.message.answer(
                f"<b>Пользователи отправившие заявку на КП:</b>\n{users_text}")
        else:
            await callback_query.message.answer(
                "Нет пользователей отправивших заявку.")
    else:
        await callback_query.message.answer(
            "У вас нет прав на выполнение этой команды.")


@router.callback_query(F.data == 'get_registered_users')
async def get_asked_price_users(callback_query: CallbackQuery,
                          dao: DataAccessObject):
    if callback_query.from_user.id in config.tg_bot.admin_ids:
        get_all_registered_users = await dao.get_all_users()
        if get_all_registered_users:
            users_text = "\n".join([
                f"User id: {user.id}, Username: {user.username}, "
                f"Fullname: {user.fullname}, Date registration: "
                f"{user.reg_date}, Email:"
                f" {user.e_mail}, Phone:"
                f" {user.phone}"
                for user in get_all_registered_users])
            await callback_query.message.answer(
                f"<b>Пользователи, зарегистрировавшиеся в боте:</b>\n{users_text}")
    else:
        await callback_query.message.answer(
            "У вас нет прав на выполнение этой команды.")
