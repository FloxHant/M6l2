import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class LeonardoAPI:
    def __init__(self):
        pass
    
    def generate_image(self):
        return 'path/to/generated_image.png'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши что-нибудь, я сгенерирую картинку!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    leonardo_api = LeonardoAPI()

    image_path = leonardo_api.generate_image()


    await update.message.reply_photo(photo=open(image_path, 'rb'))

def main():

    application = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()


    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


    application.run_polling()

if __name__ == '__main__':
    main()
