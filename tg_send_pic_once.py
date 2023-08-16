import argparse
import os

import telegram

from config import IMAGES_DIR, TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID
from file_manager import get_random_image


def main():
    bot = telegram.Bot(token=TELEGRAM_API_TOKEN)

    parser = argparse.ArgumentParser(prog='Send image to Telegram channel.')
    parser.add_argument('filename', nargs='?', help="Image name.",
                        default=get_random_image(IMAGES_DIR))
    args = parser.parse_args()
    filename = args.filename

    if filename is None:
        print('Image not found.')
        return

    image_path = os.path.join(IMAGES_DIR, filename)
    with open(image_path, 'rb') as img:
        bot.send_document(chat_id=TELEGRAM_CHAT_ID, document=img)
    print(f'{image_path} was successfully sent.')


if __name__ == '__main__':
    main()
