import datetime

from aiogram import Router, F

from aiogram.types import CallbackQuery

from DAO.data_access_object import DataAccessObject
from database import Order, Product
from keyboards.asphalt_keyboards import markup_asphalt
from keyboards.concret_sand_mix_keyboards import markup_mix
from keyboards.concrete_keyboards import markup_concrete
from keyboards.crushed_stone_keyboards import markup_crushed_granite
from keyboards.masonry_solutions_keyboards import markup_masonry
from keyboards.mounting_solution_keyboards import markup_mounting
from keyboards.sand_keyboards import markup_sand
from utils.product_id_generator import generate_unique_product_id

router: Router = Router()


# хендлеры окон нотификации при выборе товара


@router.callback_query(F.data == 'В75П3F50W2')
async def process_m100_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали бетон марки М100",
                                show_alert=True,
                                reply_markup=markup_concrete)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="бетон марки М100"
    )
    await dao.add_product(product)

    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="бетон марки М100",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=10000.00,  # цена продукта
        description="описание бетон марки М100",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'В15П4F100W4')
async def process_m200_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали бетон марки М200",
                                show_alert=True,
                                reply_markup=markup_concrete)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="бетон марки М200"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="бетон марки М200",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=11000.00,  # цена продукта
        description="описание бетон марки М200",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'В20П4F100W6')
async def process_m250_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали бетон марки М250",
                                show_alert=True,
                                reply_markup=markup_concrete)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="бетон марки М250"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="бетон марки М250",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=11500.00,  # цена продукта
        description="описание бетон марки М250",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'В225П4F150W6')
async def process_m300_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали бетон марки М300",
                                show_alert=True,
                                reply_markup=markup_concrete)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="бетон марки М300"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="бетон марки М300",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=12000.00,  # цена продукта
        description="описание бетон марки М300",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'В25П4W8F150')
async def process_m350_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали бетон марки М350",
                                show_alert=True,
                                reply_markup=markup_concrete)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="бетон марки М350"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="бетон марки М350",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=12500.00,  # цена продукта
        description="описание бетон марки М350",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'В30П4W10F200')
async def process_m400_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали бетон марки М400",
                                show_alert=True,
                                reply_markup=markup_concrete)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="бетон марки М400"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="бетон марки М400",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=13500.00,  # цена продукта
        description="описание бетон марки М400",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'РМ100ПК4')
async def process_pm100_button(callback_query: CallbackQuery,
                               dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали монтажный раствор РМ100ПК4",
                                show_alert=True,
                                reply_markup=markup_mounting)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="монтажный раствор РМ100ПК4"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="монтажный раствор РМ100ПК4",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=2,  # подкатегория продукта
        price=9500.00,  # цена продукта
        description="описание монтажный раствор РМ100ПК4",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'РМ150ПК4')
async def process_pm150_button(callback_query: CallbackQuery,
                               dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали монтажный раствор РМ150ПК4",
                                show_alert=True,
                                reply_markup=markup_mounting)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="монтажный раствор РМ150ПК4"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="монтажный раствор РМ150ПК4",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=2,  # подкатегория продукта
        price=10000.00,  # цена продукта
        description="описание монтажный раствор РМ150ПК4",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'РМ200ПК4')
async def process_pm150_button(callback_query: CallbackQuery,
                               dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали монтажный раствор РМ200ПК4",
                                show_alert=True,
                                reply_markup=markup_mounting)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="монтажный раствор РМ200ПК4"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="монтажный раствор РМ200ПК4",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=2,  # подкатегория продукта
        price=10500.00,  # цена продукта
        description="описание монтажный раствор РМ200ПК4",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'М50ПК3')
async def process_m50_button(callback_query: CallbackQuery,
                             dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали раствор кладочный М50ПК3",
                                show_alert=True,
                                reply_markup=markup_masonry)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="раствор кладочный М50ПК3"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="раствор кладочный М50ПК3",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=3,  # подкатегория продукта
        price=8500.00,  # цена продукта
        description="описание раствора кладочного М50ПК3",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'М75ПК3')
async def process_m75_button(callback_query: CallbackQuery,
                             dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали раствор кладочный М75ПК3",
                                show_alert=True,
                                reply_markup=markup_masonry)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="раствор кладочный М75ПК3"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="раствор кладочный М75ПК3",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=3,  # подкатегория продукта
        price=9000.00,  # цена продукта
        description="описание раствора кладочного М75ПК3",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'М100ПК3')
async def process_m100_button(callback_query: CallbackQuery,
                              dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали раствор кладочный М100ПК3",
                                show_alert=True,
                                reply_markup=markup_masonry)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="раствор кладочный М100ПК3"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="раствор кладочный М100ПК3",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=3,  # подкатегория продукта
        price=9500.00,  # цена продукта
        description="описание раствора кладочного М100ПК3",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_2')
async def process_csm_1_2_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/2",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/2"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/2",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=10000.00,  # цена продукта
        description="Описание ЦПС 1/2",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_3')
async def process_csm_1_3_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/3",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/3"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/3",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=9500.00,  # цена продукта
        description="Описание ЦПС 1/3",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_4')
async def process_csm_1_4_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/4",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/4"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/4",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=9000.00,  # цена продукта
        description="Описание ЦПС 1/4",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_5')
async def process_csm_1_5_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/5",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/5"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/5",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=8500.00,  # цена продукта
        description="Описание ЦПС 1/5",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_6')
async def process_csm_1_6_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/6",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/6"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/6",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=7750.00,  # цена продукта
        description="Описание ЦПС 1/6",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_7')
async def process_csm_1_7_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/7",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/7"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/7",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=7500.00,  # цена продукта
        description="Описание ЦПС 1/7",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_8')
async def process_csm_1_8_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/8",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/8"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/8",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=7250.00,  # цена продукта
        description="Описание ЦПС 1/8",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_9')
async def process_csm_1_9_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/9",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/9"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="ЦПС 1/9",  # имя продукта
        category_id=1,  # категория продукта
        subcategory_id=4,  # подкатегория продукта
        price=7000.00,  # цена продукта
        description="Описание ЦПС 1/9",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'CSM_1_10')
async def process_csm_1_10_button(callback_query: CallbackQuery,
                                  dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали ЦПС 1/10",
                                show_alert=True,
                                reply_markup=markup_mix)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="ЦПС 1/10"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Песок карьерный",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=1950.00,  # цена продукта
        description="Описание песка карьерного",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'alluvial_sand')
async def process_alluvial_sand_button(callback_query: CallbackQuery,
                                       dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали Песок намывной",
                                show_alert=True,
                                reply_markup=markup_sand)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Песок намывной"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Песок намывной",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=1800.00,  # цена продукта
        description="Описание песка намывного",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'quarry_sand')
async def process_quarry_sand_button(callback_query: CallbackQuery,
                                     dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали Песок карьерный",
                                show_alert=True,
                                reply_markup=markup_sand)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Песок карьерный"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Песок карьерный",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=1950.00,  # цена продукта
        description="Описание песка карьерного",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'crushing_sand')
async def process_crushing_sand_button(callback_query: CallbackQuery,
                                       dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали Песок из отсева дробления",
                                show_alert=True,
                                reply_markup=markup_sand)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Песок из отсева дробления"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Песок из отсева дробления",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=1,  # подкатегория продукта
        price=1250.00,  # цена продукта
        description="Описание песка из отсева дробления",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'crushed_granite_10_20')
async def process_granite_10_20_button(callback_query: CallbackQuery,
                                       dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали Щебень гранитный 10-20",
                                show_alert=True,
                                reply_markup=markup_crushed_granite)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Щебень гранитный 10-20"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Щебень гранитный 10-20",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=2,  # подкатегория продукта
        price=2100.00,  # цена продукта
        description="Описание щебня гранитного 10-20",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'crushed_granite_20_40')
async def process_granite_20_40_button(callback_query: CallbackQuery,
                                       dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали Щебень гранитный 20-40",
                                show_alert=True,
                                reply_markup=markup_crushed_granite)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Щебень гранитный 20-40"
    )
    await dao.add_product(product)

    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Щебень гранитный 20-40",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=2,  # подкатегория продукта
        price=2200.00,  # цена продукта
        description="Описание щебня гранитного 20-40",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'crushed_granite_5_10')
async def process_granite_5_10_button(callback_query: CallbackQuery,
                                      dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали Щебень гранитный 5-10",
                                show_alert=True,
                                reply_markup=markup_crushed_granite)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Щебень гранитный 5-10"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Щебень гранитный 5-10",  # имя продукта
        category_id=2,  # категория продукта
        subcategory_id=2,  # подкатегория продукта
        price=2300.00,  # цена продукта
        description="Описание щебня гранитного 5-10",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)


@router.callback_query(F.data == 'asphalt')
async def process_asphalt_button(callback_query: CallbackQuery,
                                 dao: DataAccessObject):
    await callback_query.answer(text="Вы выбрали асфальт",
                                show_alert=True,
                                reply_markup=markup_asphalt)
    product = Product(
        user_id=callback_query.from_user.id,
        product_id=generate_unique_product_id(),
        name="Асфальт"
    )
    await dao.add_product(product)
    order = Order(
        user_id=callback_query.from_user.id,
        product_id=product.product_id,
        name="Асфальт",  # имя продукта
        category_id=3,  # категория продукта
        subcategory_id=0,  # подкатегория продукта
        price=8000.00,  # цена продукта
        description="Описание асфальта",  # описание продукта
        order_date=datetime.date.today()
    )

    # Добавление продукта в заказ пользователя
    await dao.add_order(order)
