from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔄 Tarjimon'),
            KeyboardButton(text='🤖 CHAT GPT'),

        ],
        [
            KeyboardButton(text='⚙️ Sozlamalar'),
            KeyboardButton(text="📞 Bog'lanish"),

        ],
    ],
    resize_keyboard=True,
)
