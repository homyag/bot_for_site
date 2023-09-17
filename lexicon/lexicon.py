LEXICON: dict[str, str] = {
    '/start': '<b>Привет!</b> Я бот для отправки коммерческих '
              'предложений <b>ТД Ленинградский</b>.\nЧтобы ознакомиться с '
              'товарной номенклатурой нажмите кнопку <b>"номенклатура"</b> '
              'или '
              'отправьте команду '
              '/shop\nЧтобы запросить коммерческое предложение нажмите '
              'кнопку <b>"запросить КП"</b> или отправьте команду /price\n'
              'Чтобы получить справку по работе бота - отправьте '
              'команду /help',
    '/help': 'Это бот-магазин. Здесь вы можете выбрать интересующие '
             'вас товары.\n\nДоступные команды:\n/shop - перейти в '
             'каталог товаров\n/cart - посмотреть вашу корзину\n'
             '/help - справка по работе бота',
    '/shop': 'Пожалуйста, выберите интересующую Вас товар из '
             'списка ниже:',
    '/cart': 'Сейчас в вашей корзине ',
    '/contacts': 'Наш сайт: https://betonmariupol.ru \nНаша почта: '
                 'sales.betonmariupol@gmail.com \nНаш телефон: +79495632679',
    'cart_empty': 'Сейчас ваша корзина пуста',
    'back_button': '🔙 Назад',
    'cart': 'Корзина 🛒',
    'other_answer': 'Извините, увы, это сообщение мне непонятно...',
    }

LEXICON_MAIN_MENU: dict[str, str] = {
    '/help': "помощь",
    '/shop': 'перейти к выбору товаров',
    '/cart': '🛒 корзина',
    '/fillform': 'анкета, для получения КП',
    '/cancel': 'отменить заполнение анкеты',
    '/contacts': 'обратная связь',
    '/admin': 'меню администратора'
}

LEXICON_GOODS: dict[str, str] = {
    '/бетон':
            'артикул В7,5П3F50W2 - 10000 рублей/м3,\nартикул В15П4F100W4 - '
            '11000 рублей/м3,\nартикул В20П4F100W6 - 11500 рублей/м3,'
            '\nартикул В22,5П4F150W6 - 12000 рублей/м3,\nартикул В25П4W8F150 '
            '- 12500 рублей/м3,\n артикул В30П4W10F200 13500 рублей/м3\n'
        ,
    'раствор монтажный':
        [
            ['артикул РМ100ПК4', "9500 рублей/м3"],
            ['артикул РМ150ПК4', "10000 рублей/м3"],
            ['артикул РМ200ПК4', "10500 рублей/м3"],
        ],
    'раствор кладочный':
        [
            ['артикул М50ПК3', "8500 рублей/м3"],
            ['артикул М75ПК3', "9000 рублей/м3"],
            ['артикул М100ПК3', "9500 рублей/м3"],
        ],
    'цементно-песочная смесь':
        [
            ['ЦПС 1/2', "10000 рублей/м3"],
            ['ЦПС 1/3', "9500 рублей/м3"],
            ['ЦПС 1/4', "9000 рублей/м3"],
            ['ЦПС 1/5', "8500 рублей/м3"],
            ['ЦПС 1/6', "8000 рублей/м3"],
            ['ЦПС 1/7', "7750 рублей/м3"],
            ['ЦПС 1/8', "7500 рублей/м3"],
            ['ЦПС 1/9', "7250 рублей/м3"],
            ['ЦПС 1/10', "7000 рублей/м3"],
        ],
    'песок':
        [
            ['Песок намывной', "1800 рублей за тонну"],
            ['Песок карьерный', "1950 рублей за тонну"],
            ['Песок из отсева дробления', "1250 рублей за тонну"],
        ],
    'щебень':
        [
            ['Щебень гранитный 10-20', "2300 рублей за тонну"],
            ['Щебень гранитный 20-40', "2200 рублей за тонну"],
            ['Щебень гранитный 5-10', "2300 рублей за тонну"]
        ],
    'асфальтобетон':
        '<b>асфальтобетон</b>, все марки: 8000 рублей за тонну'
}
