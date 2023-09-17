from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from config_data import load_config
from keyboards.admin_keyboards import admin_keyboard
from keyboards.category_keyboard import markup_category
from keyboards.hello_keyboard import markup_hello
from lexicon.lexicon import LEXICON


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    config = load_config("bot.ini")
    if message.from_user.id in config.tg_bot.admin_ids:
        await message.answer(text=f"Привет {message.from_user.full_name}. Вы "
                                  "зарегистрированы как "
                                  "администратор. Список команд "
                                  "администратора доступен кнопками ниже.",
                             reply_markup=admin_keyboard)
    else:
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

