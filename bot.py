from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo
import logging
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Главное меню
@dp.message(Command('start'))
async def start(message: types.Message):
    web_app_url = "https://your-mini-app-url.com"  # URL вашего мини-приложения
    await message.answer(
        "Добро пожаловать в мясную лавку!",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="🛍️ Заказать", web_app=WebAppInfo(url=web_app_url))],
                [types.KeyboardButton(text="📦 Корзина")],
                [types.KeyboardButton(text="🆘 Помощь")]
            ],
            resize_keyboard=True
        )
    )

# Обработка данных из мини-приложения
@dp.message(F.content_type == 'web_app_data')
async def handle_web_app_data(message: types.Message):
    data = message.web_app_data.data
    try:
        data = eval(data)  # Преобразуем строку JSON в словарь
        if data['action'] == 'add_to_cart':
            product_id = data['productId']
            await message.answer(f"Товар с ID {product_id} добавлен в корзину!")
        elif data['action'] == 'open_cart':
            await message.answer("Переход в корзину...")
        elif data['action'] == 'help':
            await message.answer("Связь с администратором установлена!")
    except Exception as e:
        logging.error(f"Ошибка при обработке данных: {e}")
        await message.answer("Произошла ошибка!")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)