# main.py
import asyncio
from typing import List

from twikit import Tweet

from twikihelper import TwikitHelper
from tweet_handler import save_tweets
from models import create_tables


async def main():
    create_tables()

    helper = TwikitHelper(cookies_path='cookies.json')

    result: List[Tweet] = await helper.get_time_line(tweet_count=20)

    await save_tweets(result)


asyncio.run(main())
