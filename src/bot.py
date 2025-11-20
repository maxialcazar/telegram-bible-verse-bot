import requests
from telegram.ext import Updater, CommandHandler

API_URL = "https://bible-api.com/"

def languaje_list(reference):
    msg = ""
    try:
        response = requests.get(API_URL + "data")
        data = response.json()
        print(len(data["translations"]))

        if "translations" in data:
            for i in range(len(data["translations"])):
                print(data["translations"][i]["identifier"])
                identifier = data["translations"][i]["identifier"]
                name = data["translations"][i]["name"]
                msg += f"{name} - {identifier}\n"
            return msg
        else:   
            return "Languaje wasnt found."
    except:
        return "API error."

def langlist(update, context):
    reference = " ".join(context.args)
    result = languaje_list(reference)
    update.message.reply_text(result)

def get_verse(args):
    #print(arg[0], arg[1], arg[2])
    try:
        if args[0] == "random":
            req = API_URL + "data/web/random"
            response = requests.get(req)
            data = response.json()

            rverse = data["random_verse"]
            book = rverse["book"]
            chapter = rverse["chapter"]
            verse = rverse["verse"]
            text = rverse["text"].strip()
            return f"{book} {chapter}:{verse}\n\n{text}"

        if len(args) != 1:
            req = API_URL + args[0] + " " + args[1] + "?translation=" + args[2]
            response = requests.get(req)
            data = response.json()
        
        print(data)

        if "text" in data:
            book = data["reference"]
            text = data["text"].strip()
            return f"{book}\n\n{text}"
        else:
            return "Verse wasnt found."
    except Exception as e:
        print(e)
        return "API error."


def verse(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Use: /verse Jhon 3:16 WEB")
        return

    result = get_verse(context.args)
    update.message.reply_text(result)
    update.message.reply_text("Try /verse random!")

def send_long_message(update, text):
    MAX = 4096
    if len(text) <= MAX:
        update.message.reply_text(text)
        return
    
    # Enviar en partes
    for i in range(0, len(text), MAX):
        update.message.reply_text(text[i:i+MAX])

def get_chapter(args):
    book = "   "

    try:
        req = API_URL + args[0] + "+" + args[1]
        response = requests.get(req)
        data = response.json()
        book += f"  {data['reference']}\n\n"

        if  "reference" in data:
            verses = data["verses"]
            for i in range(len(verses)):
                book += f"{verses[i]['verse']}- \n   {verses[i]['text']}"
            return book
        else:
            return "Chapter wasnt found."
    except Exception as e:
        print(e)
        return "API error."

def chapter(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Use: /chapter John 6")
        return

    result = get_chapter(context.args)
    send_long_message(update, result)

def start(update, context):
    update.message.reply_text(
        "Welcome! send me a verse using:s\n/verse [book] [chapter:verse] [languaje (use /langs)]"
    )

def main():
    TOKEN = "8526595556:AAHstqn2nVK-5PDn0gzv1ouXzCUdeR7hFh4"
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verse", verse))
    dp.add_handler(CommandHandler("chapter", chapter))
    dp.add_handler(CommandHandler("langs", langlist))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
