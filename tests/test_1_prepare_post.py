import os
from models import Post, load_post_from_pickle, save_post_as_pickle
import pytest

@pytest.mark.order(0)
def test_save_post_as_pickle():
    how_many_post = 1000
    save_post_as_pickle(how_many_post)

    # check posts.pickle exists
    assert os.path.exists("posts.pickle") is True
    assert os.path.isfile("posts.pickle") is True
    assert os.path.getsize("posts.pickle") > 0

    posts = load_post_from_pickle()
    assert len(posts) == how_many_post
    assert isinstance(posts, list)
    assert isinstance(posts[0], Post)
