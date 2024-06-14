from urllib.parse import unquote
from urllib.parse import urlparse
import requests

from pathlib import Path


DIR_PATH = './images/'


def get_file_name(url):
    path = urlparse(url).path
    file_name = path.split('/')[-1]
    return unquote(file_name)


def save_image_in_dir(url, path, auth_params=None):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=auth_params)
    response.raise_for_status()
    with open(f'{path}{get_file_name(url)}', 'wb') as file:
        file.write(response.content)
