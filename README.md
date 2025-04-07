# 💱 Currency Exchange Telegram Bot

A simple Telegram bot built with `aiogram` that allows users to get exchange rates between currencies. Just send a
message like `100 USD to EUR`, and the bot will respond with the converted amount.

## 🚀 Features

- Real-time currency exchange using a free API
- Easy-to-use message format: `amount FROM_CURRENCY to TO_CURRENCY`
- List of 30 popular currency codes with their names
- Built with `aiogram` 3.x
- Fast and lightweight

## 📷 Example

```
You: 100 USD to THB  
Bot: 💱 100 USD is equal to 3600.50 THB.
```

## 🧾 Supported Currencies

The bot supports these popular currencies:

```
USD - US Dollar  
EUR - Euro  
JPY - Japanese Yen  
GBP - British Pound  
AUD - Australian Dollar  
CAD - Canadian Dollar  
CHF - Swiss Franc  
CNY - Chinese Yuan  
SEK - Swedish Krona  
NZD - New Zealand Dollar  
MXN - Mexican Peso  
SGD - Singapore Dollar  
HKD - Hong Kong Dollar  
NOK - Norwegian Krone  
KRW - South Korean Won  
INR - Indian Rupee  
BRL - Brazilian Real  
ZAR - South African Rand  
TRY - Turkish Lira  
RUB - Russian Ruble  
THB - Thai Baht  
PLN - Polish Zloty  
DKK - Danish Krone  
MYR - Malaysian Ringgit  
PHP - Philippine Peso  
IDR - Indonesian Rupiah  
AED - United Arab Emirates Dirham  
SAR - Saudi Riyal  
EGP - Egyptian Pound  
COP - Colombian Peso  
VND - Vietnamese Dong
```

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/currency-exchange-bot.git
cd currency-exchange-bot
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file and add your API keys:**

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token  
EXCHANGE_API_KEY=your_exchange_api_key
```

You can get a free exchange API key from [https://www.exchangerate-api.com](https://www.exchangerate-api.com/)

4. **Run the bot:**

```bash
python bot.py
```

## 📦 Requirements

- Python 3.7+
- `aiogram`
- `python-dotenv`
- `requests`

## 📬 Usage

Send a message in this format:

```
<amount> <FROM_CURRENCY> to <TO_CURRENCY>
```

Example:

```
250 EUR to USD
```

The bot will reply with the converted value.

## 🧑‍💻 Author

Made with ❤️ by 3dendroid,
tg: [@denisazonov](https://t.me/denisazonov)
