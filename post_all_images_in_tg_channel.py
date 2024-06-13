import telegram
from dotenv import load_dotenv

import asyncio
import os
import random
import time
import argparse

from save_images_from_urls import DIR_PATH


async def post_images_in_channel(time_sleep):
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'],)
    chat_id_env = os.environ['TELEGRAM_CHAT_ID']
    if not time_sleep:
        time_sleep = 14400
    while (True):
        images_names = os.listdir(DIR_PATH)
        random.shuffle(images_names)
        for image_name in images_names:
            async with bot:
                await bot.send_photo(
                                        chat_id=chat_id_env,
                                        photo=open(DIR_PATH+image_name, 'rb')
                                    )
            time.sleep(time_sleep)
        print(f'All images has been posted into {chat_id_env}')
        print('Reshuffle images and start posting images again...')

if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Post images in telegram channel')
    parser.add_argument('time_sleep', help='sleep time in seconds', nargs='?')
    parser = parser.parse_args()
    time_sleep = parser.time_sleep
    if time_sleep:
        time_sleep = int(time_sleep)
    asyncio.run(post_images_in_channel(time_sleep))