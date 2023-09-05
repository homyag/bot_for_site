from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.asphalt_keyboards import markup_asphalt
from keyboards.concret_sand_mix_keyboards import markup_mix
from keyboards.concrete_keyboards import markup_concrete
from keyboards.crushed_stone_keyboards import markup_crushed_granite
from keyboards.masonry_solutions_keyboards import markup_masonry
from keyboards.mounting_solution_keyboards import markup_mounting
from keyboards.sand_keyboards import markup_sand
from keyboards.subcategory_keyboard import markup_subcategory_1, \
    markup_subcategory_2, markup_subcategory_3

router: Router = Router()


# Хендлер для обработки нажатия на кнопку категории СТРОИТЕЛЬНЫЕ СМЕСИ
@router.callback_query(F.data == 'goods|1|0|0')
async def process_category_1(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_1)


# Хендлер для обработки нажатия на кнопку категории НЕРУДНЫЕ МАТЕРИАЛЫ
@router.callback_query(F.data == 'goods|2|0|0')
async def process_category_2(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_2)


@router.callback_query(F.data == 'goods|3|0|0')
async def process_category_3(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_asphalt)


# хендлер бетона
@router.callback_query(F.data == 'goods|1|1|0')
async def process_concrete_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_concrete)


# хендлер монтажного раствора
@router.callback_query(F.data == 'goods|1|2|0')
async def process_mounting_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_mounting)


# хендлер кладочного раствора
@router.callback_query(F.data == 'goods|1|3|0')
async def process_masonry_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_masonry)


# хендлер ЦПС
@router.callback_query(F.data == 'goods|1|4|0')
async def process_mix_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_mix)


# песочный хендлер
@router.callback_query(F.data == 'goods|2|1|0')
async def process_sand_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_sand)


# щебневый хендлер
@router.callback_query(F.data == 'goods|2|2|0')
async def process_sand_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_crushed_granite)


# Хендлер для обработки нажатия на кнопку категории АСФАЛЬТОБЕТОН
@router.callback_query(F.data == 'goods|3|0|0')
async def process_category_3(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_3)


# хендлеры кнопок назад к...
# ...к подкатегории 1
@router.callback_query(F.data == 'building mixes')
async def process_back_from_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_1)


# ...к подкатегории 2
@router.callback_query(F.data == 'non_metallic_materials')
async def process_back_from_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_2)