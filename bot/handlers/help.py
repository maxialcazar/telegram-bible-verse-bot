help_message = "<b>📖 Bible Bot — Help Menu</b>\n\nHere are all available commands:\n\n<b>/verse &lt;book_id&gt; &lt;chapter:verse&gt; &lt;translation_id&gt;</b>\nGet a specific verse.\nExample: /verse john 3:16 web\n\n<b>/random</b>\nGet a completely random verse 🎲\n\n<b>/chapter &lt;book_id&gt; &lt;chapter&gt;</b>\nReturn the full chapter from the selected book.\nExample: /chapter john 1\n\n<b>/langs</b>\nList all available translation IDs 🌐\n\n<b>/books</b>\nShow the list of book IDs used for /verse and /chapter 📚\n\n<b>/help</b>\nShow this help message again.\n"

async def help_command(update, context): 
    await update.message.reply_text(help_message, parse_mode="HTML")
    return