import argparse

import requests

from config import IMAGES_DIR, NASA_API_KEY
from file_manager import download_image


def fetch_nasa_apod(img_dir: str, api_key: str, count: int = 1):
    """Download NASA APOD pics via API and save them to `img_dir`."""
    params = {
        'api_key': api_key,
        'count': count,
    }
    apod_url = 'https://api.nasa.gov/planetary/apod'
    resp = requests.get(apod_url, params=params)
    resp.raise_for_status()
    apods = resp.json()
    images_saved = 0
    for media in apods:
        if media['media_type'] != 'image':
            continue
        download_image(img_dir, media['url'])
        images_saved += 1
    print(f'{images_saved} images has been saved.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Fetch NASA Pics of the Day')
    parser.add_argument('count', default=1, nargs='?',
                        help="How many pics to fetch.")
    args = parser.parse_args()
    fetch_nasa_apod(IMAGES_DIR, NASA_API_KEY, int(args.count))
