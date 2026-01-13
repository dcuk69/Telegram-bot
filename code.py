from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8291837196:AAF1oNPcaJObMGSi2ZMHtkH3mI48V2a71tI"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()

if __name__ == "__main__":
    main()
