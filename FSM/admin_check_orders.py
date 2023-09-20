from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage: MemoryStorage = MemoryStorage()

# Создаем "базу данных" пользователей
order_dict: dict[int, dict[str, str | int | bool]] = {}


# Класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMAdminOrder(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодействия с пользователем
    fill_user_name = State()  # Состояние ожидания ввода имени пользователя
    fill_phone = State()  # Состояние ожидания вводи телефона пользователя
    fill_product_name = State()  # Состояние ожидания ввода имени продукта
    fill_order_date = State()  # Состояние ожидания ввода даты заказа
