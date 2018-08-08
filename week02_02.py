import functools
import json


def to_json(func):
    result = func(*args, )
    return json.dumps(result)


@to_json
def get_data():
    return {
        'data': 42
    }

print(get_data())