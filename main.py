import asyncio
import random
import time
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from twikit import Tweet

import endpoint_request
import tweet_handler
from endpoint_request import login_request, add_post
from models import create_tables, TweetModel
from tweet_handler import save_tweets
from twikihelper import TwikitHelper

helper = TwikitHelper(cookies_path='cookies.json')


async def main():
    print("post-poster started")

    load_dotenv()

    await login_request()

    background_tasks = [
        asyncio.create_task(scheduled_get_timeline_tweets()),
        asyncio.create_task(scheduled_post_tweet())
    ]

    create_tables()

    await asyncio.gather(*background_tasks)


# todo get data every 10 to 15 min  randomly here
async def scheduled_get_timeline_tweets():
    while True:
        random_period = random.uniform(60 * 10, 60 * 15)
        after_date = datetime.fromtimestamp(datetime.now().timestamp() + random_period)

        if endpoint_request.expire_date < (time.time() * 1000):
            await login_request()
            print(f"auth token was expired. taken new auth.")
            await scheduled_get_timeline_tweets()
        else:
            print(f'random will timeline will be fetch on {after_date} min')
            await asyncio.sleep(random_period)

            result: List[Tweet] = await helper.get_time_line(tweet_count=20)

            await save_tweets(result)
            print(f'random will timeline will be completed.: {datetime.now()}')


# todo pop post every 3 to 6 min  randomly here
async def scheduled_post_tweet():
    while True:
        random_period = random.uniform(60 * 3, 60 * 6)
        after_date = datetime.fromtimestamp(datetime.now().timestamp() + random_period)

        if endpoint_request.expire_date < (time.time() * 1000):
            await login_request()
            print(f"auth token was expired. taken new auth.")
            await scheduled_get_timeline_tweets()
        else:
            print(f'tweet gonna post on. : {after_date} min.')
            await asyncio.sleep(random_period)
            r1: TweetModel = await tweet_handler.get_random_tweet()
            await endpoint_request.add_post(username=r1.user_name, content=r1.full_text)
            # get post from db
            # http request here
            # post if post id it not in posted table
            # post tweet and save id to posted table
            print(f'tweet posted. : {datetime.now()}')


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("post-poster finished.")
