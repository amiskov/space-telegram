import telegram

from config import IMAGES_DIR, TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID
from file_manager import get_random_image


def main():
    bot = telegram.Bot(token=TELEGRAM_API_TOKEN)

    filename = get_random_image(IMAGES_DIR)
    if filename is None:
        print('Pictures not found.')
        return

    bot.send_document(chat_id=TELEGRAM_CHAT_ID, document=open(filename, 'rb'))


if __name__ == '__main__':
    main()
