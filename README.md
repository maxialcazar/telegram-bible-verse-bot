# Telegram Bible Verse Bot

A Telegram bot built in Python that fetches Bible verses, chapters, and random passages using the public **Bible API**.  
Designed as a lightweight example of API integration, command handling, and bot development using `python-telegram-bot`.

---

## 📌 Features

- `/verse <book> <chapter:verse> <translation>` – Returns a specific verse.  
  Example: `/verse John 3:16 WEB`

- `/verse random` – Returns a random Bible verse.

- `/chapter <book> <chapter>` – Retrieves a full chapter, automatically split into multiple Telegram messages.

- `/langs` – Lists all available translations from the API.

- Robust error handling
- Automatic splitting of large messages (Telegram limit: 4096 chars)

---

## 🛠️ Tech Stack

- **Python 3.x**
- **python-telegram-bot**
- **requests**
- **Bible API** (https://bible-api.com)

---

## 📁 Project Structure

/
├── src/
│ ├── bot.py
│ ├── requirements.txt
│ └── README.md
---

## 🚀 Running the Bot

### 1. Install dependencies

pip install -r requirements.txt

### 2. Set your Telegram bot token

Create an environment variable or replace the placeholder inside `bot.py`:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
3. Run the bot
nginx
Copiar código
python bot.py
📌 API Used
This bot uses the free Bible API:
https://bible-api.com

🧩 Future Improvements
Add inline keyboard buttons

Add bookmarking/favorites

Add daily verse subscription

Deploy via Docker or Railway.app
```
