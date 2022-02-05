from collections.abc import Callable

from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.filters import Filters


from merch_generator import MerchGenerator, ImgProcessor, TextProcessor

class TelegramBot:
    def __init__(self, bot_url: str,):
        self.updater = Updater(bot_url, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CommandHandler('help', self.help))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self.text_message_handler))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))
        self.merch_generator = MerchGenerator(img_processor=ImgProcessor(),
                                              text_processor=TextProcessor())

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text(
            "Hello sir, Welcome to the Bot.Please write"
            "help to see the commands available."
        )

    def help(self, update: Update, context: CallbackContext):
        update.message.reply_text("Введите описание мероприятия, для которого"
                                  "вам нужен мерч")

    def unknown(self, update: Update, context: CallbackContext):
        with open('results/output.png', 'rb') as file:
            update.message.reply_photo(file)
        update.message.reply_text(
            "Sorry '%s' is not a valid command" % update.message.text)

    def text_message_handler(self, update: Update, context: CallbackContext):
        # (update.message.text)
        self.merch_generator.generate(update.message.text)
        with open('results/output сухой.png', 'rb') as file:
            update.message.reply_photo(file)

    def run(self):
        self.updater.start_polling()
