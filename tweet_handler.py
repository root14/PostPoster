from typing import List

from models import TweetModel
from twikit import Tweet


async def save_tweets(tweets: List[Tweet]):
    for tweet in tweets:
        tweet_instance, created = TweetModel.get_or_create(
            tweet_id=tweet.id,
            defaults={
                'full_text': tweet.full_text,
                'favorite_count': tweet.favorite_count,
                'view_count': tweet.view_count,
                'reply_count': tweet.reply_count,
                'user_id': tweet.user.id,
                'user_name': tweet.user.name
            }
        )


def load_tweets():
    return TweetModel.select()
