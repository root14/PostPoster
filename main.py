import asyncio
import random
from datetime import datetime
import time
from typing import List
from twikit import Tweet
from models import create_tables
from tweet_handler import save_tweets
from twikihelper import TwikitHelper


async def main():
    background_tasks = [
        asyncio.create_task(scheduled_tweets()),
        asyncio.create_task(scheduled_post_tweet())
    ]

    print(f'tool started')
    create_tables()

    helper = TwikitHelper(cookies_path='cookies.json')

    result: List[Tweet] = await helper.get_time_line(tweet_count=20)

    await save_tweets(result)

    await asyncio.gather(*background_tasks)


# todo get data every 3 to 5 min  randomly here
async def scheduled_tweets():
    while True:
        print(f'Tweets started to be received: {datetime.now()}')
        random_period = random.uniform(3, 6)
        print(random_period)
        print(f'Tweets started to be completed.: {datetime.now()}')
        await asyncio.sleep(random_period)


# todo pop post every 3 to 5 min  randomly here
async def scheduled_post_tweet():
    while True:
        print(f'Tweets started to be received: {datetime.now()}')
        random_period = random.uniform(3, 6)
        print(random_period)
        print(f'Tweets started to be completed.: {datetime.now()}')
        await asyncio.sleep(random_period)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program sonlandırıldı!")
