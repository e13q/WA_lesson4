import requests
from dotenv import load_dotenv

import os
import argparse
import random

from save_images_from_urls import save_image_in_dir
from save_images_from_urls import DIR_PATH


def fetch_image_name_with_time(date):
    url = f'https://epic.gsfc.nasa.gov/api/natural/date/{date}'
    response = requests.get(url, params={
        'api_key': os.environ['API_KEY_NASA'],
    })
    response.raise_for_status()
    response = response.json()
    image_name_with_time = response[random.randrange(len(response))]['image']
    return image_name_with_time


def get_random_indexies_from_array(array, count):
    random_indexies_from_resp = []
    for i in range(0, count):
        random_index_from_resp = random.randrange(len(array))
        while (random_index_from_resp in random_indexies_from_resp):
            random_index_from_resp = random.randrange(len(array))
        random_indexies_from_resp.append(random_index_from_resp)
    return random_indexies_from_resp


def assemble_nasa_epic_url(date, api_key_nasa):
    image_name_with_time = fetch_image_name_with_time(date)
    url_base = 'https://api.nasa.gov/EPIC/archive/natural/'
    date = date.replace('-', '/')
    url_path_with_date = f'{url_base}{date}/png/{image_name_with_time}.png'
    params_api_key = {'api_key': api_key_nasa}
    return {'url': url_path_with_date, 'params': params_api_key}


def fetch_nasa_epic(count, api_key_nasa):
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(url, params={
        'api_key': api_key_nasa,
    })
    response.raise_for_status()
    response = response.json()
    random_indexies_from_resp = get_random_indexies_from_array(response, count)
    dates = [response[index]['date'] for index in random_indexies_from_resp]
    urls_with_params = [
        assemble_nasa_epic_url(date, api_key_nasa) for date in dates
    ]
    return urls_with_params


if __name__ == '__main__':
    load_dotenv()
    api_key_nasa = os.environ['API_KEY_NASA']
    parser = argparse.ArgumentParser(
        description="Download some count of images from NASA epic")
    parser.add_argument(
        'count',
        help='count of images',
        type=int
    )
    parser = parser.parse_args()
    count = parser.count
    for urls_with_params in fetch_nasa_epic(count, api_key_nasa):
        save_image_in_dir(
            urls_with_params['url'],
            DIR_PATH,
            urls_with_params['params']
        )
    print(f'{count} images of NASA epic downloaded')
