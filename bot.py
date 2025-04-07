import asyncio
import os

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")  # Добавляем ключ для API обмена валют
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Словарь с транскрипциями для популярных валют
currency_translations = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "JPY": "Japanese Yen",
    "GBP": "British Pound",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SEK": "Swedish Krona",
    "NZD": "New Zealand Dollar",
    "MXN": "Mexican Peso",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "NOK": "Norwegian Krone",
    "KRW": "South Korean Won",
    "INR": "Indian Rupee",
    "BRL": "Brazilian Real",
    "ZAR": "South African Rand",
    "TRY": "Turkish Lira",
    "RUB": "Russian Ruble",
    "THB": "Thai Baht",
    "PLN": "Polish Zloty",
    "DKK": "Danish Krone",
    "MYR": "Malaysian Ringgit",
    "PHP": "Philippine Peso",
    "IDR": "Indonesian Rupiah",
    "AED": "United Arab Emirates Dirham",
    "SAR": "Saudi Riyal",
    "EGP": "Egyptian Pound",
    "COP": "Colombian Peso",
    "VND": "Vietnamese Dong",
}


@dp.message(CommandStart())
async def start(message: Message):
    currency_list = "\n".join([f"{key} - {value}" for key, value in currency_translations.items()])
    await message.answer(f"👋 Hello, {message.from_user.full_name}!")
    await message.answer("Send me a currency pair (e.g., '100 USD to EUR') and I'll return the exchange rate! 💱")
    await message.answer(f"Here are some popular currencies:\n\n{currency_list}")


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("📍 Send me a currency pair like '100 USD to EUR' and I'll return the exchange rate!")


@dp.message(F.text)
async def get_exchange_rate(message: Message):
    try:
        # Получаем текст с валютами
        text = message.text.strip()
        parts = text.split()

        if len(parts) != 4 or parts[2].lower() != "to":
            await message.answer(
                "⚠️ Please use the format 'amount from_currency to to_currency'. For example: '100 USD to EUR'.")
            return

        amount = float(parts[0])
        from_currency = parts[1].upper()
        to_currency = parts[3].upper()

        # Используем бесплатный API для получения курса валют
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()

        if data['result'] == "error":
            await message.answer("⚠️ Could not fetch the exchange rate. Please try again.")
            return

        # Отправляем результат
        conversion_result = data['conversion_result']
        await message.answer(f"💱 {amount} {from_currency} is equal to {conversion_result} {to_currency}.")
    except Exception as e:
        print("Error:", e)
        await message.answer("⚠️ An error occurred. Please try again.")


async def main():
    print("💱 Currency bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
