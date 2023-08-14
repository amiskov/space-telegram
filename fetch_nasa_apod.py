import argparse

import requests

from config import IMAGES_DIR, NASA_API_KEY
from file_manager import download_image


def fetch_nasa_apod(count=1):
    """Download NASA APOD pics via API"""
    params = {
        'api_key': NASA_API_KEY,
        'count': count,
    }
    apod_url = 'https://api.nasa.gov/planetary/apod'
    resp = requests.get(apod_url, params=params)
    resp.raise_for_status()
    images = resp.json()
    for img in images:
        url = img['url']
        download_image(IMAGES_DIR, url)
    print(f'{len(images)} images has been saved.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Fetch NASA Pics of the Day')
    parser.add_argument('count', default=1, nargs='?',
                        help="How many pics to fetch.")
    args = parser.parse_args()
    count = int(args.count)
    fetch_nasa_apod(count)
