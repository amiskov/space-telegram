import random
from pathlib import Path
from datetime import date

import requests
from environs import Env

from helpers import download_image

env = Env()
env.read_env()
NASA_API_KEY = env("NASA_API_KEY")


def fetch_apod(count=3):
    """
    Downloads images from NASA APOD API and saves them into `images_path`.
    """
    params = {
        'api_key': NASA_API_KEY,
        'count': count,
    }
    apod_url = 'https://api.nasa.gov/planetary/apod'
    resp = requests.get(apod_url, params=params)
    resp.raise_for_status()
    for index, img in enumerate(resp.json()):
        url = img['url']
        download_image(url)
        print(f'Image {index+1} has been saved.')


def get_epic_url_from_meta(img_meta: dict) -> str:
    img = img_meta['image']
    d = date.fromisoformat(img_meta['date'].split(' ')[0])
    return ('https://api.nasa.gov/EPIC/archive/natural/'
            f'{d.year}/{d.month:02d}/{d.day:02d}/thumbs/{img}.jpg')


def fetch_epic(count=3):
    params = {
        'api_key': NASA_API_KEY,
    }
    url_meta = 'https://api.nasa.gov/EPIC/api/natural/images'

    # fetch epic meta
    resp = requests.get(url_meta, params=params)
    resp.raise_for_status()
    images_meta = resp.json()

    # download epic images
    for img_meta in random.sample(images_meta, count):
        url = get_epic_url_from_meta(img_meta)
        download_image(url, params)


if __name__ == '__main__':
    # fetch_spacex_last_launch()
    fetch_epic(5)
    fetch_apod(random.randint(1, 3))
