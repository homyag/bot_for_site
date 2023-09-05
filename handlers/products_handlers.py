from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.concrete_keyboards import markup_concrete
from keyboards.mounting_solution_keyboards import markup_mounting
from keyboards.subcategory_keyboard import markup_subcategory_1

router: Router = Router()


# хендлер бетона
@router.callback_query(F.data == 'goods|1|1|0')
async def process_concrete_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_concrete)


@router.callback_query(F.data == 'back_from_concrete')
async  def process_back_from_concrete(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_1)


# хендлер монтажного раствора
@router.callback_query(F.data == 'goods|1|2|0')
async def process_concrete_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_mounting)


@router.callback_query(F.data == 'back_from_mounting')
async  def process_back_from_concrete(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_1)