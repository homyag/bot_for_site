from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from DAO.data_access_object import DataAccessObject


router: Router = Router()


@router.message(Command(commands=['cart']))
async def process_cart_command(message: Message, dao: DataAccessObject):
    user_id = message.from_user.id

    # Получите список заказов пользователя из базы данных
    user_orders = await dao.get_user_orders(user_id)

    if user_orders:
        # Если у пользователя есть заказы, отправьте их
        orders_text = "Список ваших заказов:\n Чтобы получить комерческое предложение " \
                           f"по выбранным позициям отправьте, пожалуста, " \
                           f"команду /fillform\n"
        for order in user_orders:
            orders_text += f"<b>Заказ</b>: {order['name']},\n Цена:" \
                           f" {order['price']} " \
                           f"руб.\n"

        await message.answer(orders_text)
    else:
        # Если у пользователя нет заказов, отправьте сообщение об этом
        await message.answer("У вас нет активных заказов.")