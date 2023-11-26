from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎥 Выбрать фильм"),
            KeyboardButton(text="📱 Лента"),
            KeyboardButton(text="🔎 Поиск фильма")
        ],
        [
            KeyboardButton(text="👤 Аккаунт"),
            KeyboardButton(text="🔝 Топы"),
        ]
    ],
    resize_keyboard=True,
)


chose_film_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Жанр"),
            KeyboardButton(text="Год")
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
        ]
    ],
    resize_keyboard=True,
)
