from aiogram import Router, F
from aiogram.types import CallbackQuery

from DAO.data_access_object import DataAccessObject

router: Router = Router()


@router.callback_query(F.data == 'get_orders')
async def get_all_orders(callback_query: CallbackQuery, dao: DataAccessObject):
    orders = await dao.get_all_orders_with_user_data()
    if orders:
        grouped_orders = {}

        for order in orders:
            username = order['username']
            if username not in grouped_orders:
                grouped_orders[username] = {
                    'phone': order['phone'],
                    'orders': []
                }

            grouped_orders[username]['orders'].append(order['name'])

        orders_text = "\n".join([
            f"Заказчик: {username}, Телефон: {data['phone']} Заказы: {', '.join(data['orders'])}"
            for username, data in grouped_orders.items()
        ])

        await callback_query.message.answer(f"Список заказов:\n{orders_text}")
    else:
        await callback_query.message.answer("Список заказов пуст.")