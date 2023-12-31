import argparse

import requests

from config import IMAGES_DIR
from file_manager import download_image


def fetch_spacex_launch(img_dir: str, launch_id='latest'):
    """Download pics of the SpaceX launch via API."""
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    resp = requests.get(url)
    resp.raise_for_status()
    images_urls = resp.json()['links']['flickr']['original']

    if not images_urls:
        print(f"There's no images for the launch with id `{launch_id}`.")

    for url in images_urls:
        download_image(img_dir, url)

    print(f'{len(images_urls)} images has been saved.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Fetch SpaceX Pics')
    parser.add_argument('launch_id', default='latest', nargs='?',
                        help="SpaceX launch ID (latest by default).")
    args = parser.parse_args()
    launch_id = args.launch_id
    fetch_spacex_launch(IMAGES_DIR, launch_id)
