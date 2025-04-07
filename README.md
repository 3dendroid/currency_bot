# 💱 Telegram Currency Bot

A simple Telegram bot using **Aiogram 3** that provides exchange rates using the [CurrencyAPI.net](https://currencyapi.net) service.

## 🚀 Features

- `/start` — Intro message
- `/help` — How to use the bot
- Send a currency like `USD` or pair like `USD/EUR` — get exchange rate

## 🔧 Tech Stack

- Python 3.10+
- Aiogram 3
- CurrencyAPI.net

## 📦 Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/currency-bot.git
cd currency-bot
```

2. Create `.env` file with your keys:
```
TELEGRAM_BOT_TOKEN=your_telegram_token
CURRENCY_API_KEY=your_currencyapi_key
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the bot:
```bash
python bot.py
```

## ☁️ Deploy on Railway

- Connect the repo to [Railway](https://railway.app)
- Set environment variables
- Done!