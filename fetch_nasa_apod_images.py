import requests
from dotenv import load_dotenv

import os
import argparse

from save_images_from_urls import save_image_in_dir
from save_images_from_urls import DIR_PATH


def fetch_nasa_apod(count, api_key_nasa):
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params={
        'api_key': api_key_nasa,
        'count': count,
    })
    response.raise_for_status()
    urls = []
    for info_of_image in response.json():
        urls.append(info_of_image['url'])
    return urls


if __name__ == '__main__':
    load_dotenv()
    api_key_nasa = os.environ['API_KEY_NASA']
    parser = argparse.ArgumentParser(
        description="Download some count of images from NASA apod")
    parser.add_argument(
        'count',
        help='count of images',
        type=int
    )
    parser = parser.parse_args()
    count = parser.count
    for url in fetch_nasa_apod(count, api_key_nasa):
        save_image_in_dir(url, DIR_PATH)
    print(f'{count} images of NASA apod downloaded')
