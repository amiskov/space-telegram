import random
from pathlib import Path
from datetime import date

import requests
from environs import Env

from helpers import *

env = Env()
env.read_env()
NASA_API_KEY = env("NASA_API_KEY")


def fetch_spacex_last_launch(images_path: Path):
    """
    Downloads images from SpaceX API and saves them into `images_path`.
    """
    resp = requests.get(
        'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    images_urls = resp.json()['links']['flickr']['original']
    for index, url in enumerate(images_urls):
        download_image(url, images_path)
        print(f'Image {index+1} of {len(images_urls)} has been',
              f'saved to {images_path}.')


def fetch_apod(images_path: Path, count: int):
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
        download_image(url, images_path)
        print(f'Image {index+1} has been saved to {images_path}.')


def download_image(url: str, path: Path, params=None) -> None:
    """
    `url` must have an image file extension at the end.

    Картинки можно называть так: spacex1.jpg, spacex2.jpg и так далее. Для генерации индексов картинки лучше использовать enumerate.
    Не забудьте указать расширение файла: .jpg.
    """
    filename = url.split('/')[-1]

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path.joinpath(filename), 'wb') as file:
        file.write(response.content)
        print(f'{filename} has been saved.')


def get_epic_url_from_meta(img_meta: dict) -> str:
    img = img_meta['image']
    d = date.fromisoformat(img_meta['date'].split(' ')[0])
    return ('https://api.nasa.gov/EPIC/archive/natural/'
            f'{d.year}/{d.month:02d}/{d.day:02d}/thumbs/{img}.jpg')


def fetch_epic(path: Path, count=5):
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
        download_image(url, path, params)


if __name__ == '__main__':
    images_path = Path('images')
    images_path.mkdir(exist_ok=True)
    fetch_spacex_last_launch(images_path)
    fetch_epic(images_path, 5)
    fetch_apod(images_path, random.randint(1, 3))
