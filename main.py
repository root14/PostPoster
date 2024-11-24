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


# todo get data every 10 to 15 min  randomly here
async def scheduled_tweets():
    while True:
        random_period = random.uniform(60 * 10, 60 * 15)
        print(f'random will timeline will be fetch on {random_period} min')
        print(f'random_period {random_period}')

        await asyncio.sleep(random_period)
        # http request here
        print(f'random will timeline will be completed.: {datetime.now()}')


# todo pop post every 3 to 6 min  randomly here
async def scheduled_post_tweet():
    while True:
        random_period = random.uniform(60 * 3, 60 * 6)
        print(f'random_period {random_period}')
        print(f'tweet gonna post on. : {datetime.now()} min.')

        await asyncio.sleep(random_period)
        # http request here
        print(f'tweet posted. : {datetime.now()}')


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Postposter finished.")
