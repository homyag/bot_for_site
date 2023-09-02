from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int


category_1: InlineKeyboardButton = InlineKeyboardButton(
                    text='СТРОЙМАТЕРИАЛЫ',
                    callback_data=GoodsCallbackFactory(
                                            category_id=1,
                                            subcategory_id=0,
                                            item_id=0).pack())

category_2: InlineKeyboardButton = InlineKeyboardButton(
                    text='НЕРУДНЫЕ МАТЕРИАЛЫ',
                    callback_data=GoodsCallbackFactory(
                                            category_id=2,
                                            subcategory_id=0,
                                            item_id=0).pack())

category_3: InlineKeyboardButton = InlineKeyboardButton(
                    text='АСФАЛЬТОБЕТОН',
                    callback_data=GoodsCallbackFactory(
                                            category_id=3,
                                            subcategory_id=0,
                                            item_id=0).pack())

markup: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[category_1],
                                     [category_2],
                                     [category_3]])
