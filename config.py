import logging

from environs import Env

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


env = Env()
env.read_env()

IMAGES_DIR = env('IMAGES_DIR', 'images')
NASA_API_KEY = env('NASA_API_KEY')
TELEGRAM_API_TOKEN = env('TELEGRAM_API_TOKEN')
TELEGRAM_CHAT_ID = env('TELEGRAM_CHAT_ID')
POSTING_TIMEOUT_SEC = env.timedelta('POSTING_TIMEOUT_SEC', 4*60*60)
