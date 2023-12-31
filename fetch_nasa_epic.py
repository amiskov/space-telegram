import argparse
import random
from datetime import date

import requests

from config import IMAGES_DIR, NASA_API_KEY
from file_manager import download_image

EPIC_BASE_URL = 'https://api.nasa.gov/EPIC'


def fetch_nasa_epic(img_dir: str, api_key: str, count: int = 3):
    """Download EPIC photo via NASA API."""
    params = {
        'api_key': api_key,
    }
    url_meta = f'{EPIC_BASE_URL}/api/natural/images'

    # Fetch EPIC images meta.
    resp = requests.get(url_meta, params=params)
    resp.raise_for_status()
    images_meta = resp.json()

    # Download several random EPIC images.
    count = min(len(images_meta), count)
    sample_images = random.sample(images_meta, count)
    for img_meta in sample_images:
        url = get_image_url(img_meta)
        download_image(img_dir, url, params)


def get_image_url(img_meta: dict) -> str:
    """Return an API URL for an image based on its meta info."""
    img = img_meta['image']
    d = date.fromisoformat(img_meta['date'].split(' ')[0])
    return (f'{EPIC_BASE_URL}/archive/natural/'
            f'{d.year}/{d.month:02d}/{d.day:02d}/png/{img}.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Fetch NASA EPIC image.')
    parser.add_argument('count', default=1, nargs='?',
                        help="How many pics to fetch.")
    args = parser.parse_args()
    fetch_nasa_epic(IMAGES_DIR, NASA_API_KEY, int(args.count))
