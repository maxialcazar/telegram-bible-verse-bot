import requests
import config

async def search_command(update, context):
    try:
        if not context.args:
            await update.message.reply_text(
                "Uso: /search <texto>\nEj: /search Jesús sanó"
            )
            return

        query = " ".join(context.args)
        url = f"{config.API_URL}search?query={query}"

        response = requests.get(url)
        data = response.json()

        results = data.get("results", [])

        if not results:
            await update.message.reply_text("No se encontraron resultados.")
            return

        # Mostrar los primeros 3 resultados para no saturar
        message = "Resultados:\n\n"
        for r in results[:3]:
            ref = r.get("reference", "")
            text = r.get("text", "")
            message += f"{ref}\n{text}\n\n"

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
