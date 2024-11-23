from typing import List

from models import TweetModel, UserModel
from twikit import Tweet


async def save_tweets(tweets: List[Tweet]):
    for tweet in tweets:
        user, created = UserModel.get_or_create(
            id=tweet.user.id,
            defaults={'name': tweet.user.name}
        )

        tweet_instance, created = TweetModel.get_or_create(
            tweet_id=tweet.id,
            defaults={
                'full_text': tweet.full_text,
                'favorite_count':tweet.favorite_count,
                'view_count':tweet.view_count,
                'reply_count':tweet.reply_count,
                'user': user,
            }
        )

def load_tweets():
    return TweetModel.select()
