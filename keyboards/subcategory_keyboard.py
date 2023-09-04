from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.callback_class import GoodsCallbackFactory

back_button = InlineKeyboardButton(
    text='Назад',
    callback_data='back_to_category'
)

subcategory_1_1: InlineKeyboardButton = InlineKeyboardButton(
                    text='БЕТОН',
                    callback_data=GoodsCallbackFactory(
                                            category_id=1,
                                            subcategory_id=1,
                                            item_id=0).pack())

subcategory_1_2: InlineKeyboardButton = InlineKeyboardButton(
                    text='РАСТВОР МОНТАЖНЫЙ',
                    callback_data=GoodsCallbackFactory(
                                            category_id=1,
                                            subcategory_id=2,
                                            item_id=0).pack())

subcategory_1_3: InlineKeyboardButton = InlineKeyboardButton(
                    text='РАСТВОР КЛАДОЧНЫЙ',
                    callback_data=GoodsCallbackFactory(
                                            category_id=1,
                                            subcategory_id=3,
                                            item_id=0).pack())

subcategory_1_4: InlineKeyboardButton = InlineKeyboardButton(
                    text='ЦЕМЕНТНО-ПЕСОЧНАЯ СМЕСЬ',
                    callback_data=GoodsCallbackFactory(
                                            category_id=1,
                                            subcategory_id=4,
                                            item_id=0).pack())

markup_subcategory_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[subcategory_1_1],
                                     [subcategory_1_2],
                                     [subcategory_1_3],
                                     [subcategory_1_4],
                                     [back_button]])

subcategory_2_1: InlineKeyboardButton = InlineKeyboardButton(
                    text='ПЕСОК',
                    callback_data=GoodsCallbackFactory(
                                            category_id=2,
                                            subcategory_id=1,
                                            item_id=0).pack())

subcategory_2_2: InlineKeyboardButton = InlineKeyboardButton(
                    text='ЩЕБЕНЬ',
                    callback_data=GoodsCallbackFactory(
                                            category_id=2,
                                            subcategory_id=2,
                                            item_id=0).pack())

markup_subcategory_2: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[subcategory_2_1],
                                     [subcategory_2_2],
                                     [back_button]])

subcategory_3_1: InlineKeyboardButton = InlineKeyboardButton(
                    text='АСФАЛЬТОБЕТОН',
                    callback_data=GoodsCallbackFactory(
                                            category_id=3,
                                            subcategory_id=1,
                                            item_id=0).pack())

markup_subcategory_3: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[subcategory_3_1],
                                     [back_button]])

markup_subcategory_3_1: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[back_button]])
