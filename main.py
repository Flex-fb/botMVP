from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Укажи переменную окружения на хостинге

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("✍️ Написать менеджеру", url="https://t.me/finance_creditt"),
        InlineKeyboardButton("🧑‍💻 Подписаться на канал", url="https://t.me/financ_credit")
    )
    welcome_text = (
        "Здравствуйте, уважаемый клиент!\n\n"
        "Вы попали в бот компании *Finance Credit*,\n"
        "нажмите пожалуйста кнопку написать менеджеру или подписаться на канал 👇👇👇"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
