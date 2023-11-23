import json
import orjson
import pytest

from models import load_post_from_pickle

post_store = load_post_from_pickle()

# pylint: disable=no-member, line-too-long

@pytest.mark.order('last')
def test_deserialize_and_compare():
    posts = post_store
    json_dump_results = {
        str(i): json.dumps(post.model_dump()) for i, post in enumerate(posts)
    }
    orjson_dump_results = {
        str(i): orjson.dumps(post.model_dump()) for i, post in enumerate(posts)
    }

    for i in range(len(posts)):
        assert json_dump_results[str(i)] != orjson_dump_results[str(i)]

    for i in range(len(posts)):
        assert orjson.loads(json_dump_results[str(i)]) == orjson.loads(orjson_dump_results[str(i)])
        assert orjson.loads(json_dump_results[str(i)]) == json.loads(json_dump_results[str(i)])
        assert orjson.loads(json_dump_results[str(i)]) == json.loads(orjson_dump_results[str(i)])
        assert orjson.loads(orjson_dump_results[str(i)]) == json.loads(json_dump_results[str(i)])
        assert orjson.loads(orjson_dump_results[str(i)]) == json.loads(orjson_dump_results[str(i)])
        assert json.loads(json_dump_results[str(i)]) == json.loads(orjson_dump_results[str(i)])
