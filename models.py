from peewee import *

db = SqliteDatabase('tweets.db')


class BaseModel(Model):
    class Meta:
        database = db


class TweetModel(BaseModel):
    tweet_id = CharField(unique=True)
    full_text = TextField()
    favorite_count = IntegerField()
    view_count = TextField(null=True)
    user_id = CharField()
    user_name = CharField()


class PostedPost(BaseModel):
    posted_post_id = CharField(unique=True)


def create_tables():
    with db:
        db.create_tables([TweetModel, PostedPost])
