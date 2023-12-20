import requests
import aiohttp

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.default.main import main
from keyboards.inline.lang import lang
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom Hushkelibsiz: 🇺🇿 ▶️ 🇷🇺", reply_markup=main)
    await message.answer(f"Iltimos uzingizga kerakli bo'lgan tilni tanlang.\n Misol: 🇺🇿 ▶️ 🇷🇺", reply_markup=lang)


async def translator(frm="auto", to="uz", text="Xato"):
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

    payload = {
        "from": frm,
        "to": to,
        "text": text
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "5f494f4ab5msh1cb5cae5f817f1ap130291jsn5e213ba6595d",
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers) as response:
            result = await response.json()
            print(result)  # Add this line to inspect the result structure

            # Extracting the first translation if available
            translation = result.get('trans', None)

            return translation

# Import necessary modules and classes

# ... (your existing code)

# Import necessary modules and classes

# ... (your existing code)
# ... (your existing code)

# ... (your existing code)

@dp.callback_query_handler(lambda callback: True)
async def save_callback_message(callback: types.CallbackQuery, state: FSMContext):
    # Extract relevant information from the callback message
    chosen_language_code = callback.data  # Use callback.data to get the chosen language code
    chat_id = callback.message.chat.id
    user_id = callback.message.from_user.id

    # Save the information using the state proxy
    async with state.proxy() as data:
        data['chosen_language_code'] = chosen_language_code
        data['chat_id'] = chat_id
        data['user_id'] = user_id

    # Do something with the saved information
    print(f"Chosen Language Code: {chosen_language_code}")
    print(f"Chat ID: {chat_id}, User ID: {user_id}")

    # Answer the first callback query
    await callback.answer()

    # Set a flag in the state to indicate that the first question is answered
    await state.update_data(first_question_answered=True)

    # Ask the second question
    await callback.message.answer(f'Tanlandi: {chosen_language_code}. Qaysi tilga o\'girasiz?', reply_markup=lang)

    return False


@dp.callback_query_handler(lambda callback: True)
async def save_to_callback_message(callback: types.CallbackQuery, state: FSMContext):
    # Extract relevant information from the callback message
    async with state.proxy() as data:
        chosen_language_code = data.get('chosen_language_code', 'auto')  # Default to 'uz' if not found
        first_question_answered = data.get('first_question_answered', False)

    chosen_to_language_code = callback.data  # Use callback.data to get the chosen language code
    chat_id = callback.message.chat.id
    user_id = callback.message.from_user.id

    # Save the information using the state proxy with the correct key
    async with state.proxy() as data:
        data['chosen_to_language_code'] = chosen_to_language_code  # Use the correct key

    # Do something with the saved information
    print(f"Chosen Language Code: {chosen_to_language_code}")
    print(f"Chat ID: {chat_id}, User ID: {user_id}")

    # Answer the second callback query
    await callback.answer()

    if first_question_answered:
        # Ask the third question or perform other actions
        await callback.message.answer(
            f'Tanlandi: {chosen_language_code}, Qaysi tilga o\'girasiz: {chosen_to_language_code}. \n <b>Endi Iltimis MATN kiriting',
            reply_markup=lang)
    else:
        # Handle the case where the second question is answered before the first
        await callback.message.answer(f'Please answer the first question before answering this one.')


# ... (your existing code)

# ... (your existing code)

# ... (your existing code)


# ... (your existing code)


@dp.message_handler(lambda message: True)
async def save_message(message: types.Message, state: FSMContext):
    # Save the message text to a variable
    saved_message = message.text
    async with state.proxy() as data:
        chosen_language_code = data.get('chosen_language_code', 'auto')  # Default to 'uz' if not found
        chosen_to_language_code = data.get('chosen_to_language_code', 'ru')  # Default to 'uz' if not found

    # You can also save other message properties if needed
    chat_id = message.chat.id
    user_id = message.from_user.id
    translation_info = await translator(chosen_language_code, chosen_to_language_code, saved_message)
    print(translation_info)
    await message.answer(text=f"<i>{saved_message}</i>:\n <b>{translation_info}</b>")
    # Do something with the saved message or variables
    print(f"Saved Message: {saved_message} ,{chosen_language_code} , {chosen_to_language_code}")
    print(f"Chat ID: {chat_id}, User ID: {user_id}")

    # If you want to use the saved message in another part of your code or handler
    async with state.proxy() as data:
        data['saved_message'] = saved_message
        data['chat_id'] = chat_id
        data['user_id'] = user_id

    # You can now access these values later in your code through the state proxy
