import pickle
from datetime import datetime

from faker import Faker
from pydantic import BaseModel

faker = Faker(locale="ko_KR")


class User(BaseModel):
    name: str
    email: str
    password: str


class Post(BaseModel):
    title: str
    content: str
    created_at: str
    updated_at: str
    deactivated_at: datetime = None
    deactivated: bool = False
    published: bool = False
    author: User
    categories: list = []
    tags: list = []


def make_user():
    return User(name=faker.name(), email=faker.email(), password=faker.password())


def make_post(count: int = 1):
    return [
        Post(
            title=faker.sentence(),
            content=faker.text(),
            author=make_user(),
            categories=[faker.word() for _ in range(3)],
            tags=[faker.word() for _ in range(3)],
            created_at=faker.iso8601(),
            updated_at=faker.iso8601(),
        )
        for _ in range(count)
    ]


def save_post_as_pickle(count: int = 1000):
    posts = make_post(count=count)
    with open("posts.pickle", "wb") as f:
        pickle.dump(posts, f)


def load_post_from_pickle():
    with open("posts.pickle", "rb") as f:
        posts = pickle.load(f)
    return posts
