import telegram
from dotenv import load_dotenv
import asyncio


import os


async def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'],)
    async with bot:
        await bot.send_message(
                                text='Hello World!',
                                chat_id=os.environ['TELEGRAM_CHAT_ID']
                            )


if __name__ == '__main__':
    asyncio.run(main())
