from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎥 Choose film"),
            KeyboardButton(text="📱 FilmTok"),
            KeyboardButton(text="🔎 Film search")
        ],
        [
            KeyboardButton(text="👤 Account"),
            KeyboardButton(text="🔝 Top"),
        ]
    ],
    resize_keyboard=True,
)


chose_film_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gener"),
            KeyboardButton(text="Year"),
        ],
        [
            KeyboardButton(text="⬅️ Back"),
        ]
    ],
    resize_keyboard=True,
)
