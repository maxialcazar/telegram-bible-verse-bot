from telegram import Update
from telegram.ext import ContextTypes
from bot.services.bible_service import get_verse

async def verse_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Uso: /verse Juan 3:16")
        return

    query = " ".join(context.args)

    result = await get_verse(query)

    if not result:
        await update.message.reply_text("No pude encontrar ese versículo.")
        return

    await update.message.reply_text(result)
