from email.policy import default

from models import TweetModel, PostedPost


async def save_post(tweet: TweetModel):
    PostedPost.get_or_create(
        defaults={
            'posted_post_id': tweet.tweet_id
        }
    )


async def check_if_posted_b4(tweet_id: str):
    return PostedPost.select().where(PostedPost.posted_post_id == tweet_id).exists()
