from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from lexicon.lexicon import LEXICON

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


@router.message(Command(commands=['shop']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/shop'])

