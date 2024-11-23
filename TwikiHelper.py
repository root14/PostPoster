from typing import List
from twikit import Client, Tweet


class TwikitHelper(object):
    client = Client(language='en-Us')

    def __init__(self, cookies_path):
        self._cookies_path = cookies_path
        self.client.load_cookies(cookies_path)

    async def get_user_by_id(self, userid):
        try:
            result = await self.client.get_user_by_id(user_id=userid)
            return result
        except Exception as e:
            print(f"error -> {e}")
            raise e

    async def get_time_line(self, tweet_count=20) -> List[Tweet]:
        try:
            result = await self.client.get_timeline(count=tweet_count)
            tweets: List[Tweet] = []
            for tweet in result:
                tweets.append(tweet)

            return tweets
        except Exception as e:
            print(f"error -> {e}")
            raise e

    async def get_user_tweets(self, userid, tweet_type='Tweets', count=20):
        try:
            result = await self.client.get_user_tweets(user_id=userid, tweet_type=tweet_type, count=count)
            return result
        except Exception as e:
            print(f"error -> {e}")
            raise e

    async def get_tweet_by_id(self, tweetid):
        try:
            result = await self.client.get_tweet_by_id(tweetid)
            return result
        except Exception as e:
            print(f"error -> {e}")
            raise e
