import telegram
from dotenv import load_dotenv
import asyncio


import os


async def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'],)
    async with bot:
        await bot.send_photo(
                                chat_id=os.environ['TELEGRAM_CHAT_ID'],
                                photo=open('./images/swan_rheman.jpg', 'rb')
                            )


if __name__ == '__main__':
    asyncio.run(main())
