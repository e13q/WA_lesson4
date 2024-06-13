import telegram
from dotenv import load_dotenv

import asyncio
import os
import argparse
import random

from save_images_from_urls import DIR_PATH


async def post_image_in_channel(image_path):
    if not image_path:
        images_names = os.listdir(DIR_PATH)
        random.shuffle(images_names)
        image_path = DIR_PATH + images_names[0]
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'],)
    async with bot:
        await bot.send_photo(
                                chat_id=os.environ['TELEGRAM_CHAT_ID'],
                                photo=open(image_path, 'rb')
                            )

if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Post image in telegram channel')
    parser.add_argument('image_path', help='path to image', nargs='?')
    parser = parser.parse_args()
    image_path = parser.image_path
    asyncio.run(post_image_in_channel(image_path))
    print(f'Image has been posted into {os.environ['TELEGRAM_CHAT_ID']}')
