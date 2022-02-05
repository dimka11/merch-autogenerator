import config  # create file config.py with your personal telegram_bot_url
from app import TelegramBot

if __name__ == "__main__":
    app = TelegramBot(bot_url=config.telegram_bot_url)
    app.run()
