from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from keyboards.category_keyboard import markup_category
from keyboards.hello_keyboard import markup_hello
from keyboards.subcategory_keyboard import markup_subcategory_1, \
    markup_subcategory_2, markup_subcategory_3, markup_subcategory_3_1
from lexicon.lexicon import LEXICON, LEXICON_GOODS

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=markup_hello)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


@router.message(Command(commands=['shop']))
async def process_shop_command(message: Message):
    await message.answer(text=LEXICON['/shop'], reply_markup=markup_category)


# Хендлер для обработки нажатия кнопки "номенклатура"
@router.callback_query(F.data == 'nomenclature_pressed')
async def process_back_button(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=LEXICON['/shop'],
        reply_markup=markup_category)


# Хендлер для обработки нажатия кнопки "Назад"
@router.callback_query(F.data == 'back_to_category')
async def process_back_button(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_category)


@router.callback_query(F.data == 'back_to_main')
async def process_back_to_main_button(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text='Вы можете ознакомиться с ассортиментом или запросить '
             'коммерческое предложение',
        reply_markup=markup_hello)


# Хендлер для обработки нажатия на кнопку категории СТРОЙМАТЕРИАЛЫ
@router.callback_query(F.data == 'goods|1|0|0')
async def process_category_1(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_1)


# Хендлер для обработки нажатия на кнопку категории НЕРУДНЫЕ МАТЕРИАЛЫ
@router.callback_query(F.data == 'goods|2|0|0')
async def process_category_2(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_2)


# Хендлер для обработки нажатия на кнопку категории АСФАЛЬТОБЕТОН
@router.callback_query(F.data == 'goods|3|0|0')
async def process_category_3(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(
        reply_markup=markup_subcategory_3)

