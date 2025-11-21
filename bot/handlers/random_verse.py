import requests
from bot.config import API_URL

async def random_command(update, context):
    try:
        response = requests.get(f"{API_URL}data/web/random")
        data = response.json()

        verse = data.get("text", "")
        reference = data.get("reference", "")

        if not verse:
            await update.message.reply_text("No se pudo obtener un versículo aleatorio.")
            return

        await update.message.reply_text(f"{reference}\n\n{verse}")

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
