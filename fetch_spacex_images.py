import requests

import argparse

from save_images_from_urls import save_image_in_dir
from save_images_from_urls import DIR_PATH


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download images from last or specific SpaceX launch')
    parser.add_argument(
        'launch_id',
        help='launch id (optional)',
        nargs='?',
        default='5eb87ce5ffd86e000604b339'
    )
    parser = parser.parse_args()
    launch_id = parser.launch_id
    for url in fetch_spacex_last_launch(launch_id):
        save_image_in_dir(url, DIR_PATH)
    print('SpaceX launch images are downloaded')
