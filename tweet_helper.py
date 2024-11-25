import random
from typing import List

from models import TweetModel, PostedPost
from twikit import Tweet


# TweetModel.get_by_id(pk=2)
# TweetModel.select().count()
async def get_random_tweet():
    post_count = TweetModel.select().count()
    random_post = random.randint(1, post_count)
    # release memory
    post_count = None
    return TweetModel.get_by_id(random_post)


async def save_tweets(tweets: List[Tweet]):
    for tweet in tweets:
        tweet_instance, _ = TweetModel.get_or_create(
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
