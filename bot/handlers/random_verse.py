import requests
import config

async def random_command(update, context):
    try:
        # Si tu API es diferente, decime la ruta y lo cambio
        response = requests.get(f"{config.API_URL}random")
        data = response.json()

        verse = data.get("text", "")
        reference = data.get("reference", "")

        if not verse:
            await update.message.reply_text("No se pudo obtener un versículo aleatorio.")
            return

        await update.message.reply_text(f"{reference}\n\n{verse}")

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
