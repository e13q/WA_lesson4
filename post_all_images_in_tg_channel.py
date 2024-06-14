import telegram
from dotenv import load_dotenv

import asyncio
import os
import random
import time
import argparse

from save_images_from_urls import DIR_PATH


async def post_images_in_channel(time_sleep, chat_id_tg, token_bot_tg):
    bot = telegram.Bot(token=token_bot_tg)
    if not time_sleep:
        time_sleep = 14400
    while (True):
        images_names = os.listdir(DIR_PATH)
        random.shuffle(images_names)
        for image_name in images_names:
            async with bot:
                await bot.send_photo(
                    chat_id=chat_id_tg,
                    photo=open(f'{DIR_PATH}{image_name}', 'rb')
                )
            time.sleep(time_sleep)
        print(f'All images has been posted into {chat_id_tg}')
        print('Reshuffle images and start posting images again...')

if __name__ == '__main__':
    load_dotenv()
    chat_id_tg = os.environ['TELEGRAM_CHAT_ID']
    token_bot_tg = os.environ['TELEGRAM_BOT_TOKEN']
    parser = argparse.ArgumentParser(
        description='Post images in telegram channel')
    parser.add_argument(
        'time_sleep',
        help='sleep time in seconds',
        nargs='?',
        type=int
    )
    parser = parser.parse_args()
    time_sleep = parser.time_sleep
    if time_sleep:
        time_sleep = int(time_sleep)
    asyncio.run(post_images_in_channel(time_sleep, chat_id_tg, token_bot_tg))
