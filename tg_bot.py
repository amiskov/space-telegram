import os
import random

import telegram
from environs import Env


def get_random_filename(dir: str) -> str:
    filename = random.choice(os.listdir(dir))
    return f'{dir}/{filename}'


def main():
    env = Env()
    env.read_env()
    TELEGRAM_API_TOKEN = env('TELEGRAM_API_TOKEN')
    TELEGRAM_CHAT_ID = env('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=TELEGRAM_API_TOKEN)
    bot.send_document(chat_id=TELEGRAM_CHAT_ID,
                      document=open(get_random_filename('images'), 'rb'))


if __name__ == '__main__':
    main()
