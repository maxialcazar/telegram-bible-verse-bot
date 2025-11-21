import requests
from bot.config import API_URL

async def chapter_command(update, context):
    try:
        if len(context.args) != 3:
            await update.message.reply_text(
                "Uso: /chapter <idioma> <libro> <capítulo>\nEj: /chapter ES ReinaValera 1"
            )
            return

        lang = context.args[0]
        book = context.args[1]
        chapter = context.args[2]

        url = f"{API_URL}chapter/{lang}/{book}/{chapter}"
        response = requests.get(url)
        data = response.json()

        if "chapter_text" not in data:
            await update.message.reply_text("No se encontró el capítulo solicitado.")
            return

        # Si es muy largo lo dividimos en mensajes
        text = data["chapter_text"]

        # Telegram tiene límites → 4096 chars
        for i in range(0, len(text), 4096):
            await update.message.reply_text(text[i:i+4096])

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
