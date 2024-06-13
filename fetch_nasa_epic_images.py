import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

import os
import argparse
import random

from save_images_from_urls import save_images_in_dir
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
    for i in range(0, int(count)):
        random_index_from_resp = random.randrange(len(array))
        while (random_index_from_resp in random_indexies_from_resp):
            random_index_from_resp = random.randrange(len(array))
        random_indexies_from_resp.append(random_index_from_resp)
    return random_indexies_from_resp


def fetch_nasa_epic(count):
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(url, params={
                                        'api_key': os.environ['API_KEY_NASA'],
                                    })
    response.raise_for_status()
    response = response.json()
    random_indexies_from_resp = get_random_indexies_from_array(response, count)
    dates = []
    for index in random_indexies_from_resp:
        dates.append(response[index]['date'])
    urls = []
    for date in dates:
        image_name_with_time = fetch_image_name_with_time(date)
        url_base = 'https://api.nasa.gov/EPIC/archive/natural/'
        date = date.replace('-', '/')
        url_path_with_date = f'{date}/png/{image_name_with_time}.png?'
        params = urlencode({'api_key': os.environ['API_KEY_NASA']})
        url = url_base + url_path_with_date + params
        urls.append(url)
    return urls


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Download some count of images from NASA epic")
    parser.add_argument('count', help='count of images')
    parser = parser.parse_args()
    count = parser.count
    load_dotenv()
    for url in fetch_nasa_epic(count):
        save_images_in_dir(url, DIR_PATH)
    print(f'{count} images of NASA epic downloaded')
