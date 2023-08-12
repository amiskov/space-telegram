import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def get_extension_from_url(url: str) -> str | None:
    """
    >>> get_extension_from_url('https://example.com/txt/hello%20world.txt?v=9#python')
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


def download_image(url: str, params=None) -> None:
    """
    `url` must have an image file extension at the end.

    Картинки можно называть так: spacex1.jpg, spacex2.jpg и так далее. Для генерации индексов картинки лучше использовать enumerate.
    Не забудьте указать расширение файла: .jpg.
    """
    images_path = Path('images')
    images_path.mkdir(exist_ok=True)

    filename = url.split('/')[-1]

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(images_path.joinpath(filename), 'wb') as file:
        file.write(response.content)
        print(f'{filename} has been saved.')
