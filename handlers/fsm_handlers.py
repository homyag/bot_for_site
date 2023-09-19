from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from DAO.data_access_object import DataAccessObject
from FSM.user_states_for_price import FSMFillForm, user_dict
from config_data import load_config
from database import User
from keyboards.fsm_keyboard import markup_start_fsm
from keyboards.hello_keyboard import markup_hello
from utils.send_notification_to_admins import send_notification

router: Router = Router()


# Этот хэндлер будет срабатывать на кнопку "запросить КП" вне состояний
# и предлагать перейти к заполнению анкеты, нажав кнопку "да"
@router.callback_query(F.data == 'price_requested', StateFilter(default_state))
async def process_price_command(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text='Для отправки нами коммерческого предложения оставьте,'
             '\nпожалуйста, свои координаты. Если Вы согласны, нажмите '
             'кнопку "да" или введите команду /fillform.\nЕсли вы хотите '
             'прервать заполнение анкеты - отправьте команду /cancel',
        reply_markup=markup_start_fsm)


# Этот хендлер обрабатывает нажатие кнопки "нет" и возвращает в меню выбора
# ассортимента или запроса КП
@router.callback_query(F.data == 'no_i_didnt_agree')
async def process_back_to_main_button(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text='Вы можете ознакомиться с ассортиментом или запросить '
             'коммерческое предложение',
        reply_markup=markup_hello)


# Этот хэндлер будет срабатывать на команду "/cancel" в состоянии
# по умолчанию и сообщать, что эта команда работает внутри машины состояний
@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text='Отменять нечего. Вы не начали заполнение '
                              'анкеты.\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /fillform')


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Вы отменили заполнение анкеты.\n\n'
                              'Если Вы хотите получить КП, то снова '
                              'перейдите к заполнению анкеты, отправив '
                              'команду /fillform')
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()


@router.callback_query(F.data == 'yes_i_agree_button')
async def process_fillform_command_from_yes(callback_query: CallbackQuery,
                                            state:
                                            FSMContext):
    await callback_query.message.edit_text(text='Пожалуйста, введите ваше '
                                                'имя.\nЕсли вы хотите прервать заполнение анкеты - отправьте команду /cancel')
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)


# Этот хэндлер будет срабатывать на команду /fillform
# и переводить бота в состояние ожидания ввода имени
@router.message(Command(commands='fillform'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text='Пожалуйста, введите ваше имя')
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)


# Этот хэндлер будет срабатывать, если введено корректное имя
# и переводить в состояние ожидания ввода e-mail
@router.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext,
                            dao: DataAccessObject):
    # Сохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)

    # Получаем данные пользователя из состояния
    user_data = await state.get_data()
    user_id = message.from_user.id

    # Получаем пользователя из базы данных
    existing_user = await dao.get_object(User, user_id)

    if existing_user:
        # Если пользователь существует, обновляем его телефон
        existing_user.name = user_data.get("name")
    await dao.session.commit()

    await message.answer(text='Спасибо!\n\nА теперь введите ваш e-mail')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.fill_mail)


# Этот хэндлер будет срабатывать, если во время ввода имени
# будет введено что-то некорректное
@router.message(StateFilter(FSMFillForm.fill_name))
async def warning_not_name(message: Message):
    await message.answer(text='То, что вы отправили не похоже на имя\n\n'
                              'Пожалуйста, введите ваше имя\n\n'
                              'Если вы хотите прервать заполнение анкеты - '
                              'отправьте команду /cancel')


# Этот хэндлер переводит в состояние ввода e-mail и ожидания ввода
# телефонного номера
@router.message(StateFilter(FSMFillForm.fill_mail))
async def process_mail_sent(message: Message, state: FSMContext,
                            dao: DataAccessObject):
    # Сохраняем почту в хранилище по ключу "mail"
    await state.update_data(mail=message.text)
    # Получаем данные пользователя из состояния
    user_data = await state.get_data()
    user_id = message.from_user.id

    # Получаем пользователя из базы данных
    existing_user = await dao.get_object(User, user_id)

    if existing_user:
        # Если пользователь существует, обновляем его телефон
        existing_user.e_mail = user_data.get("mail")
    await dao.session.commit()

    await message.answer(text='Спасибо!\n\nУкажите Ваш номер телефона')
    # Устанавливаем состояние ожидания ввода телефонного номера
    await state.set_state(FSMFillForm.fill_phone)


# Этот хэндлер переводит в состояние ввода телефонного номера
@router.message(StateFilter(FSMFillForm.fill_phone))
async def process_phone_sent(message: Message, state: FSMContext,
                             dao: DataAccessObject):
    config = load_config('bot.ini')
    admin_ids = config.tg_bot.admin_ids
    # Сохраняем телефон в хранилище по ключу "phone"
    await state.update_data(phone=message.text)

    # Получаем данные пользователя из состояния
    user_data = await state.get_data()
    user_id = message.from_user.id

    # Получаем пользователя из базы данных
    existing_user = await dao.get_object(User, user_id)

    if existing_user:
        # Если пользователь существует, обновляем его телефон
        existing_user.phone = user_data.get("phone")
    await dao.session.commit()

    user_dict[message.from_user.id] = await state.get_data()
    notification_text = "Получен новый запрос на КП"
    await send_notification(message.bot, admin_ids, notification_text)
    # Завершаем машину состояний
    await state.clear()
    # Уведомление админов о новом запросе на КП
    await message.answer(text='Спасибо, Ваши данные сохранены!\nНаши '
                              'менеджеры свяжутся с Вами в ближайшее '
                              'время!\n\nВы можете посмотреть '
                              'введенные данные командой /showdata\n. Для '
                              'перехода к номенклатуре введите команду /shop')


# Этот хэндлер будет срабатывать на отправку команды /showdata
# и отправлять в чат данные анкеты, либо сообщение об отсутствии данных
@router.message(Command(commands='showdata'), StateFilter(default_state))
async def process_showdata_command(message: Message):
    # Отправляем пользователю анкету, если она есть в "базе данных"
    if message.from_user.id in user_dict:
        await message.answer(
            text=f'Имя: {user_dict[message.from_user.id]["name"]}\n'
                 f'E-mail: {user_dict[message.from_user.id]["mail"]}\n'
                 f'Телефон: {user_dict[message.from_user.id]["phone"]}\n')
    else:
        # Если анкеты пользователя в базе нет - предлагаем заполнить
        await message.answer(text='Вы еще не заполняли анкету. '
                                  'Чтобы приступить - отправьте '
                                  'команду /fillform')


# Этот хэндлер будет срабатывать на любые сообщения, кроме тех
# для которых есть отдельные хэндлеры, вне состояний
@router.message(StateFilter(default_state))
async def send_echo(message: Message):
    await message.reply(text='Извините, я не понимаю этой команды')
