from peewee import *

db = SqliteDatabase('tweets.db')


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    id = CharField(unique=True)  # User ID
    name = CharField()  # User Name


class TweetModel(BaseModel):
    tweet_id = CharField(unique=True)
    full_text = TextField()
    favorite_count = IntegerField()
    view_count = TextField()
    reply_count = IntegerField()
    user = ForeignKeyField(UserModel, backref='tweets')


def create_tables():
    with db:
        db.create_tables([UserModel, TweetModel])
