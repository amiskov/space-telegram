import argparse
import logging
import random
import time
from datetime import timedelta

import telegram

from config import (IMAGES_DIR, POSTING_TIMEOUT_SEC, TELEGRAM_API_TOKEN,
                    TELEGRAM_CHAT_ID)
from file_manager import get_dir_images


def main():
    bot = telegram.Bot(token=TELEGRAM_API_TOKEN)

    parser = argparse.ArgumentParser(
        prog='Send pics to Telegram periodically.')
    parser.add_argument('period', default=POSTING_TIMEOUT_SEC, nargs='?',
                        help="How many pics to fetch.")
    args = parser.parse_args()
    period = args.period if isinstance(args.period, timedelta) \
        else timedelta(seconds=int(args.period))

    pics = get_dir_images(IMAGES_DIR)
    if not pics:
        print("Images not found.")
        return

    while True:
        shuffled_pics = random.sample(pics, len(pics))
        send_files_periodically(bot, TELEGRAM_CHAT_ID, shuffled_pics, period)


def send_files_periodically(bot: telegram.Bot, chat_id: str, files: list[str],
                            period: timedelta):
    """Send each file from `files` via `bot` to `chat_id` with `period`.

    Removes a file path from `files` after sending. Stops when `files`
    list is empty.
    """
    files_count = len(files)
    logging.info(f'Start sending {files_count} files.')
    while len(files) > 0:
        file = files.pop()
        bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
        logging.info(f'{file} sent, {len(files)} files remains.')
        time.sleep(period.total_seconds())
    logging.info(f'{files_count} are sent.')


if __name__ == '__main__':
    main()
