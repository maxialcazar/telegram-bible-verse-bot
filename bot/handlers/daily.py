import requests 
from bot.config import API_URL

async def daily_command(update, context):
    try:
        response = requests.get(f"{API_URL}daily")
        data = response.json()

        verse = data.get("text", "")
        reference = data.get("reference", "")

        if not verse:
            await update.message.reply_text("No se pudo obtener el versículo del día.")
            return

        await update.message.reply_text(f"{reference}\n\n{verse}")

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def send_daily_verse(context):
    chat_id = context.job.chat_id

    try:
        response = requests.get(f"{config.API_URL}daily")
        data = response.json()

        verse = data.get("text", "")
        reference = data.get("reference", "")

        await context.bot.send_message(chat_id, f"{reference}\n\n{verse}")

    except Exception:
        pass
