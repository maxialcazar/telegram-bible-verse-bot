from telegram.ext import Application, CommandHandler
from bot.handlers.chapter import chapter_command
from bot.handlers.verse import verse_command
from bot.handlers.langs import langs_command
from bot.handlers.random_verse import random_command
from bot.handlers.books_id import books_command
from bot.handlers.help import help_command

from bot.config import TOKEN


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("verse", verse_command))
    app.add_handler(CommandHandler("chapter", chapter_command))
    app.add_handler(CommandHandler("langs", langs_command))
    app.add_handler(CommandHandler("random", random_command))
    app.add_handler(CommandHandler("books", books_command))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
