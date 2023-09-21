# Что умеет этот бот

- Приветствие пользователя [✓]
- Добавление пользователя в БД: [✓]
  - телеграм id [✓]
  - юзернейм [✓]
  - полное имя (фамилия, имя) [✓]
  - запрос на заполнение анкеты и обновление даты пользователей в БД [✓]
  - добавлять заказ пользователя в БД [✓]
- Админ-панель [✓]

#TODO
функция обработки заказа админом (перенос активного заказа в обработанные)

# Установка

'''
git clone git@github.com:homyag/bot_for_site.git
'''

'''
python3 -m venv venv
'''

'''
source venv/bin/activate
'''

'''
sudo apt install python3-pip
'''

'''
pip install -r requirements.txt
'''

## Установка postgresql

## Инициализация alembic

- Для синхронной базы данных:
alembic init [path]
Example: alembic init migration
- Для асинхронной базы данных:
alembic init -t async [path]
Example: alembic init -t async migration
