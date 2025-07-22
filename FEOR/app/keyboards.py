from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

#Главная клавиатура
inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '📨Выбрать общину', callback_data = 'communities'),
    InlineKeyboardButton(text = '❓Задать вопрос \nФонду', callback_data = 'feedback')],
])

# communities = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text = 'Община 1', callback_data = 'community_1')],
#     [InlineKeyboardButton(text = 'Община 2', callback_data = 'community_2')],
#     [InlineKeyboardButton(text = 'Община 3', callback_data = 'community_3')],
#     [InlineKeyboardButton(text = 'Община 4', callback_data = 'community_4')],
#     [InlineKeyboardButton(text = 'Община 5', callback_data = 'community_5')],
#     [InlineKeyboardButton(text = 'Община 6', callback_data = 'community_6')],
#     [InlineKeyboardButton(text = 'Община 7', callback_data = 'community_7')],
#     [InlineKeyboardButton(text = 'Община 8', callback_data = 'community_8')],
# ])

# async def community_builder():
#     communities=['community_1','community_2','community_3',
#                  'community_4','community_5','community_6',
#                  'community_7','community_8','community_9']
#     keyboard = InlineKeyboardBuilder()
#     for community in communities:
#         keyboard.add(InlineKeyboardButton(text=community, callback_data=f"community_{community}"))
#     return keyboard.adjust(2).as_markup()


communities = [
    'Астрахань', 'Биробиджан', 'Бобруйск',
    'Брест ', 'Брянск', 'Владивосток',
    'Волгоград', 'Волжский', 'Воронеж',
    'Гомель', 'Гродно', 'Дербент',
    'Евпатория', 'Екатеринбург', 'Иваново',
    'Казань', 'Калуга', 'Кемерово',
    'Кострома', 'Краснодар', 'Красноярск',
    'Липецк', 'Минск', 'Могилев',
    'Москва.Бейт Хабад', 'Москва.Геула', 'Москва.ЦемахЦедек',
    'Москва.Шамир Перово', 'Мытищи', 'Нальчик',
    'Нижний Новгород', 'Новокузнецк', 'Новосибирск',
    'Обнинск', 'Орел', 'Оренбург',
    'Пенза', 'Пермь', 'Пятигорск',
    'Ростов-на-Дону', 'Самара', 'C.-Петербург.Бенци Липскер',
    'C.-Петербург.Дани Аш', 'C.-Петербург.Шмуэль Хитрик', 'Саратов',
    'Симферополь', 'Смоленск', 'Таганрог',
    'Тольятти', 'Томск', 'Тула',
    'Тюмень', 'Уфа', 'Челябинск', 'Ярославль'
    
]

ITEMS_PER_PAGE = 12  # Количество кнопок на странице

# Определяем класс для callback_data пагинации
class CommunityPageCallback(CallbackData, prefix='comm_page'):
    page: int

# Функция построения клавиатуры для конкретной страницы
async def community_builder(page: int = 0):
    keyboard = InlineKeyboardBuilder()
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    current_slice = communities[start:end]
    
    for community in current_slice:
        keyboard.button(text=community, callback_data=f"community_{community}")
    
    # Кнопки навигации
    nav_buttons = []
    if page > 0:
        nav_buttons.append(
            InlineKeyboardButton(
                text='⬅️ Назад',
                callback_data=CommunityPageCallback(page=page - 1).pack()
            )
        )
    if end < len(communities):
        nav_buttons.append(
            InlineKeyboardButton(
                text='Вперед ➡️',
                callback_data=CommunityPageCallback(page=page + 1).pack()
            )
        )
    
    if nav_buttons:
        keyboard.row(*nav_buttons)
    
    keyboard.adjust(2)
    return keyboard.as_markup()

#Клавиатура "в начало"
back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В начало', callback_data='communities')]
])