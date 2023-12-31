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
        try:
            random.shuffle(pics)
            send_files_periodically(bot, TELEGRAM_CHAT_ID, pics, period)
        except telegram.error.NetworkError as e:
            timeout = 5
            logging.error(e)
            logging.info(f'Retry in {timeout} seconds...')
            time.sleep(timeout)


def send_files_periodically(bot: telegram.Bot, chat_id: str, files: list[str],
                            period: timedelta):
    """Send each file from `files` via `bot` to `chat_id` with `period`."""
    logging.info(f'Start sending {len(files)} files.')
    files_remain = len(files)
    for file in files:
        with open(file, 'rb') as img:
            bot.send_document(chat_id=chat_id, document=img)
            files_remain -= 1
            logging.info(f'{file} sent, {files_remain} files remain.')
        time.sleep(period.total_seconds())
    logging.info(f'All {len(files)} files are sent.')


if __name__ == '__main__':
    main()
