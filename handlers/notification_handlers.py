from aiogram import Router, F

from aiogram.types import CallbackQuery

from keyboards.asphalt_keyboards import markup_asphalt
from keyboards.concret_sand_mix_keyboards import markup_mix
from keyboards.concrete_keyboards import markup_concrete
from keyboards.crushed_stone_keyboards import markup_crushed_granite
from keyboards.masonry_solutions_keyboards import markup_masonry
from keyboards.mounting_solution_keyboards import markup_mounting
from keyboards.sand_keyboards import markup_sand

router: Router = Router()


# хендлеры окон нотификации при выборе товара


@router.callback_query(F.data == 'В75П3F50W2')
async def process_m100_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали бетон марки М100",
                                show_alert=True,
                                reply_markup=markup_concrete)


@router.callback_query(F.data == 'В15П4F100W4')
async def process_m200_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали бетон марки М200",
                                show_alert=True,
                                reply_markup=markup_concrete)


@router.callback_query(F.data == 'В20П4F100W6')
async def process_m250_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали бетон марки М250",
                                show_alert=True,
                                reply_markup=markup_concrete)


@router.callback_query(F.data == 'В225П4F150W6')
async def process_m300_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали бетон марки М300",
                                show_alert=True,
                                reply_markup=markup_concrete)


@router.callback_query(F.data == 'В25П4W8F150')
async def process_m350_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали бетон марки М350",
                                show_alert=True,
                                reply_markup=markup_concrete)


@router.callback_query(F.data == 'В30П4W10F200')
async def process_m400_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали бетон марки М400",
                                show_alert=True,
                                reply_markup=markup_concrete)


@router.callback_query(F.data == 'РМ100ПК4')
async def process_pm100_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали монтажный раствор РМ100ПК4",
                                show_alert=True,
                                reply_markup=markup_mounting)


@router.callback_query(F.data == 'РМ150ПК4')
async def process_pm150_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали монтажный раствор РМ150ПК4",
                                show_alert=True,
                                reply_markup=markup_mounting)


@router.callback_query(F.data == 'РМ200ПК4')
async def process_pm150_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали монтажный раствор РМ200ПК4",
                                show_alert=True,
                                reply_markup=markup_mounting)


@router.callback_query(F.data == 'М50ПК3')
async def process_m50_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали раствор кладочный М50ПК3",
                                show_alert=True,
                                reply_markup=markup_masonry)


@router.callback_query(F.data == 'М75ПК3')
async def process_m75_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали раствор кладочный М75ПК3",
                                show_alert=True,
                                reply_markup=markup_masonry)


@router.callback_query(F.data == 'М100ПК3')
async def process_m100_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали раствор кладочный М100ПК3",
                                show_alert=True,
                                reply_markup=markup_masonry)


@router.callback_query(F.data == 'CSM_1_2')
async def process_csm_1_2_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/2",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_3')
async def process_csm_1_3_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/3",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_4')
async def process_csm_1_4_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/4",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_5')
async def process_csm_1_5_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/5",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_6')
async def process_csm_1_6_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/6",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_7')
async def process_csm_1_7_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/7",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_8')
async def process_csm_1_8_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/8",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_9')
async def process_csm_1_9_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/9",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'CSM_1_10')
async def process_csm_1_10_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали ЦПС 1/10",
                                show_alert=True,
                                reply_markup=markup_mix)


@router.callback_query(F.data == 'alluvial_sand')
async def process_alluvial_sand_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали Песок намывной",
                                show_alert=True,
                                reply_markup=markup_sand)


@router.callback_query(F.data == 'quarry_sand')
async def process_quarry_sand_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали Песок карьерный",
                                show_alert=True,
                                reply_markup=markup_sand)


@router.callback_query(F.data == 'crushing_sand')
async def process_crushing_sand_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали Песок из отсева дробления",
                                show_alert=True,
                                reply_markup=markup_sand)


@router.callback_query(F.data == 'crushed_granite_10_20')
async def process_granite_10_20_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали Щебень гранитный 10-20",
                                show_alert=True,
                                reply_markup=markup_crushed_granite)


@router.callback_query(F.data == 'crushed_granite_20_40')
async def process_granite_20_40_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали Щебень гранитный 20-40",
                                show_alert=True,
                                reply_markup=markup_crushed_granite)


@router.callback_query(F.data == 'crushed_granite_5_10')
async def process_granite_5_10_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали Щебень гранитный 5-10",
                                show_alert=True,
                                reply_markup=markup_crushed_granite)


@router.callback_query(F.data == 'asphalt')
async def process_asphalt_button(callback_query: CallbackQuery):
    await callback_query.answer(text="Вы выбрали асфальт",
                                show_alert=True,
                                reply_markup=markup_asphalt)