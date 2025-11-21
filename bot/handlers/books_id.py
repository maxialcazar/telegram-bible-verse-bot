import requests
from bot.config import API_URL

async def books_command(update, context):
    try:
        response = requests.get(API_URL + "data/web")
        data = response.json()

        if "books" not in data:
            await update.message.reply_text("No se encontraron traducciones disponibles.")
            return
        
        message = "Idiomas disponibles:\n\n"

        for item in data["books"]:
            identifier = item.get("id", "??")
            name = item.get("name", "Sin nombre")
            message += f"• {identifier} — {name}\n"

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"Error al obtener idiomas: {e}")
