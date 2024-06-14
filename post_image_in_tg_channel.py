import telegram
from dotenv import load_dotenv

import asyncio
import os
import argparse
import random

from save_images_from_urls import DIR_PATH


async def post_image_in_channel(image_path, chat_id_tg, token_bot_tg):
    if not image_path:
        images_names = os.listdir(DIR_PATH)
        random.shuffle(images_names)
        image_path = images_names[0]
    bot = telegram.Bot(token=token_bot_tg,)
    async with bot:
        await bot.send_photo(
                chat_id=chat_id_tg,
                photo=open(f'{DIR_PATH}{image_path}', 'rb')
            )

if __name__ == '__main__':
    load_dotenv()
    chat_id_tg = os.environ['TELEGRAM_CHAT_ID']
    token_bot_tg = os.environ['TELEGRAM_BOT_TOKEN']
    parser = argparse.ArgumentParser(
        description='Post image in telegram channel')
    parser.add_argument(
        'image_path',
        help='path to image',
        nargs='?'
    )
    parser = parser.parse_args()
    image_path = parser.image_path
    asyncio.run(post_image_in_channel(image_path, chat_id_tg, token_bot_tg))
    print(f'Image has been posted into {chat_id_tg}')
