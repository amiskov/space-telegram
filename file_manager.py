import logging
import os
import random
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def get_dir_images(dir: str, max_size: int = 20*1024*1024) -> list[str]:
    """Return a list of paths to images with size less than `max_size`."""
    images = []
    for path, _, file_names in os.walk(dir):
        for file_name in file_names:
            if not is_image(file_name):
                continue
            image_path = os.path.join(path, file_name)
            image_size = os.path.getsize(image_path)
            if image_size <= max_size:
                images.append(os.path.join(path, file_name))
    return images


def get_random_image(dir: str) -> str | None:
    """Return a random image path relative to the given directory.

    get_random_filename('pics') # 'pics/some_pic.jpg'
    get_random_filename('dir_without_images') # None
    """
    images = get_dir_images(dir)
    if not images:
        return None
    return random.choice(images)


def get_extension_from_url(url: str) -> str | None:
    """
    >>> get_extension_from_url('https://hey.co/hello%20world.txt?v=9#python')
    '.txt'
    >>> get_extension_from_url('https://example.com/txt/hello.png')
    '.png'
    >>> get_extension_from_url('/txt/hello.png')
    '.png'
    >>> get_extension_from_url('https://example.com/txt/hello') is None
    True
    """
    uri_path_unquoted = unquote(urlsplit(url).path)
    _, filename = os.path.split(uri_path_unquoted)
    _, ext = os.path.splitext(filename)
    return ext if ext != '' else None


def download_image(dir: str, url: str, params=None) -> None:
    """Download an image by `url` to `dir`.

    `url` must have a file extension at the end (`.png`, `.jpg`, etc).
    """
    response = requests.get(url, params=params)
    response.raise_for_status()

    images_path = Path(dir)
    images_path.mkdir(exist_ok=True)

    filename = url.split('/')[-1]
    with open(images_path.joinpath(filename), 'wb') as file:
        file.write(response.content)
        logging.info(f'{filename} has been saved.')


def is_image(file_name: str) -> bool:
    return file_name.lower().endswith(('.jpg', '.jpeg', '.gif', '.png'))
