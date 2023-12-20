from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✍️ Auto", callback_data="auto"),
            InlineKeyboardButton("🇦🇫 AF", callback_data="af"),
            InlineKeyboardButton("🇸🇦 Arab", callback_data="ar"),
            InlineKeyboardButton("🇦🇸 AS", callback_data="as"),
        ],
        [
            InlineKeyboardButton("🇹🇷 Tur", callback_data="tur"),
            InlineKeyboardButton("🇺🇿 UZ", callback_data="uz"),
            InlineKeyboardButton("🇷🇺 РУС", callback_data="ru"),
            InlineKeyboardButton("🇺🇸 ENG", callback_data="en")
        ]

    ],

)
