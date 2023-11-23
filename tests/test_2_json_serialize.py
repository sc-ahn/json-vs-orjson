import json
import logging
import time
import pytest

from models import load_post_from_pickle

json_progress_by_count = {}

post_store = load_post_from_pickle()

@pytest.mark.order(1)
def test_1_post_serialize():
    posts = post_store[:1]
    previous = time.time()
    result = {str(i): json.dumps(post.model_dump()) for i, post in enumerate(posts)}
    progress_time = time.time() - previous
    logging.info("[json.dumps] progress time: %s", progress_time)
    logging.info("[json.dumps] <%s: %s>", type(result), result)
    json_progress_by_count["1"] = progress_time * 1000

@pytest.mark.order(2)
def test_10_post_serialize():
    posts = post_store[:10]
    previous = time.time()
    _ = {str(i): json.dumps(str(post.model_dump())) for i, post in enumerate(posts)}
    progress_time = time.time() - previous
    logging.info("[json.dumps] progress time: %s", progress_time)
    json_progress_by_count["10"] = progress_time * 1000

@pytest.mark.order(3)
def test_100_post_serialize():
    posts = post_store[:100]
    previous = time.time()
    _ = {str(i): json.dumps(str(post.model_dump())) for i, post in enumerate(posts)}
    progress_time = time.time() - previous
    logging.info("[json.dumps] progress time: %s", progress_time)
    json_progress_by_count["100"] = progress_time * 1000

@pytest.mark.order(4)
def test_1000_post_serialize():
    posts = post_store
    previous = time.time()
    _ = {str(i): json.dumps(str(post.model_dump())) for i, post in enumerate(posts)}
    progress_time = time.time() - previous
    logging.info("[json.dumps] progress time: %s", progress_time)
    json_progress_by_count["1000"] = progress_time * 1000

    json.dump(
        json_progress_by_count,
        open("json_progress_by_count.json", "w", encoding="utf-8"),
    )
