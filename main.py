import asyncio
import logging
import random
import time
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from twikit import Tweet

import endpoint_request
import posted_post_helper
import tweet_helper
from endpoint_request import login_request, add_post
from models import create_tables, TweetModel, PostedPost
from tweet_helper import save_tweets
from twikihelper import TwikitHelper

helper = TwikitHelper(cookies_path='cookies.json')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("post-poster started")
    # logger.debug("auth token was expired. taken new auth.")

    load_dotenv()

    await login_request()

    background_tasks = [
        asyncio.create_task(scheduled_get_timeline_tweets()),
        asyncio.create_task(scheduled_post_tweet())
    ]

    create_tables()

    await asyncio.gather(*background_tasks)


async def scheduled_get_timeline_tweets():
    while True:
        random_period = random.uniform(60 * 10, 60 * 15)
        after_date = datetime.fromtimestamp(datetime.now().timestamp() + random_period)

        if endpoint_request.expire_date < (time.time() * 1000):
            await login_request()
            # print(f"auth token was expired. taken new auth.")
            logging.info("auth token was expired. taken new auth.")
            await scheduled_get_timeline_tweets()
        else:
            print(f'random will timeline will be fetch on {after_date} min')
            await asyncio.sleep(random_period)

            result: List[Tweet] = await helper.get_time_line(tweet_count=20)

            await save_tweets(result)
            logging.info(f'random timeline fetch completed.: {datetime.now()}')


async def scheduled_post_tweet():
    while True:
        random_period = random.uniform(60 * 3, 60 * 6)
        after_date = datetime.fromtimestamp(datetime.now().timestamp() + random_period)

        if endpoint_request.expire_date < (time.time() * 1000):
            await login_request()
            logging.info(f"auth token was expired. taken new auth.")
            await scheduled_get_timeline_tweets()
        else:
            print(f'tweet gonna post on. : {after_date} min.')
            await asyncio.sleep(random_period)
            # get post from db
            r1: TweetModel = await tweet_helper.get_random_tweet()

            if not await posted_post_helper.check_if_posted_b4(r1.tweet_id):
                await endpoint_request.add_post(username=r1.user_name, content=r1.full_text)
                await posted_post_helper.save_post(r1)
            else:
                await scheduled_get_timeline_tweets()

            # post tweet and save id to posted table
            logging.info(f'tweet posted. : {datetime.now()}')


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("post-poster finished.")
