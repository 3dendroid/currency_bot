import os
import requests
import re  # Для работы с регулярными выражениями
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# /start command
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👋 Hello, {message.from_user.full_name}!")
    await message.answer("Send me a currency code like USD or EUR, and I will show you the exchange rate to USD 💵")


# /help command
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Available commands:",
            "/start - Start the bot",
            "/help - Show help",
            "Send a message like 'USD', 'EUR', etc., to get the exchange rate to USD")
    await message.answer("\n".join(text))


# Handling currency input and fetching the exchange rate to USD
@dp.message_handler()
async def get_currency_rate(message: types.Message):
    # Используем регулярное выражение для извлечения валюты
    match = re.match(r"(\d+(\.\d+)?)?\s*([A-Za-z]{3})", message.text.strip())

    if match:
        currency_code = match.group(3).upper()  # Валютный код
    else:
        await message.answer("⚠️ Invalid input. Please enter a number and currency code like '1000 USD'.")
        return

    url = f"https://currencyapi.net/api/v1/rates?key={CURRENCY_API_KEY}&base=USD&output=JSON"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("success") and currency_code in data["rates"]:
            rate = data["rates"][currency_code]
            await message.answer(f"💱 1 USD = {rate} {currency_code}")
        else:
            await message.answer("⚠️ Couldn't fetch rate. Please check the currency code.")
    except Exception as e:
        print("Error:", e)
        await message.answer("❌ Error fetching exchange rate. Try again later.")


# Run the bot
if __name__ == '__main__':
    print("💸 Currency Bot is running...")
    executor.start_polling(dp)
