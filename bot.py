import asyncio
import logging
import os

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Logging
logging.basicConfig(level=logging.DEBUG)

# Tokens
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

# Bot initialization
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Popular currencies
currency_translations = {
    "USD": "US Dollar", "EUR": "Euro", "JPY": "Japanese Yen", "GBP": "British Pound",
    "AUD": "Australian Dollar", "CAD": "Canadian Dollar", "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan", "SEK": "Swedish Krona", "NZD": "New Zealand Dollar",
    "MXN": "Mexican Peso", "SGD": "Singapore Dollar", "HKD": "Hong Kong Dollar",
    "NOK": "Norwegian Krone", "KRW": "South Korean Won", "INR": "Indian Rupee",
    "BRL": "Brazilian Real", "ZAR": "South African Rand", "TRY": "Turkish Lira",
    "RUB": "Russian Ruble", "THB": "Thai Baht", "PLN": "Polish Zloty",
    "DKK": "Danish Krone", "MYR": "Malaysian Ringgit", "PHP": "Philippine Peso",
    "IDR": "Indonesian Rupiah", "AED": "UAE Dirham", "SAR": "Saudi Riyal",
    "EGP": "Egyptian Pound", "COP": "Colombian Peso", "VND": "Vietnamese Dong",
}


@dp.message(CommandStart())
async def start(message: Message):
    currency_list = "\n".join([f"🔹 <b>{key}</b> - {value}" for key, value in currency_translations.items()])
    await message.answer(f"👋🏼 Hello, <b>{message.from_user.full_name}</b>!")
    await message.answer("🚀 Send me a currency pair like <b>100 USD to EUR</b>, and I’ll give you the exchange rate!")
    await message.answer(f"Here are some popular currencies you can use:\n\n{currency_list}")


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("ℹ️ Just send a message like <b>100 USD to EUR</b> to get the exchange rate.")


@dp.message(F.text)
async def get_exchange_rate(message: Message):
    try:
        text = message.text.strip()
        parts = text.split()

        if len(parts) != 4 or parts[2].lower() != "to":
            await message.answer("❌ Please use the format: <b>amount FROM to TO</b>\nExample: <b>100 USD to EUR</b>")
            return

        amount = float(parts[0])
        from_currency = parts[1].upper()
        to_currency = parts[3].upper()

        if from_currency not in currency_translations or to_currency not in currency_translations:
            await message.answer("❗ Unsupported currency. Please use popular ones from the list.")
            return

        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()

        if data.get('result') == "error" or 'conversion_result' not in data:
            await message.answer("⚠️ Failed to fetch exchange rate. Please try again later.")
            return

        result = data['conversion_result']
        await message.answer(
            f"✅ <b>{amount} {from_currency}</b> 🟰 <b>{result} {to_currency}</b>\n"
        )

    except ValueError:
        await message.answer("❌ Please make sure the amount is a number. Example: <b>100 USD to EUR</b>")
    except Exception as e:
        print(f"Exception occurred: {e}")
        logging.exception("Unexpected error occurred:")
        await message.answer("🚨 An unexpected error occurred. Please try again later.")


async def main():
    logging.info("🔄 Currency bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
