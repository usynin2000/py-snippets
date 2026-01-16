from functools import partial
import json
import urllib.parse


# 1. Working with JSON


def save_to_file(data, filename, indent=2, ensure_ascii=False):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)


# Making special funcs for saving files
save_config = partial(save_to_file, filename="config.json")
save_logs = partial(save_to_file, filename="logs.json")
save_pretty = partial(save_to_file, filename="pretty.json", indent=4)


data = {"name": "Alice", "age": 30, "city": "Москва"}

save_config(data)
save_logs({"event": "user_login", "timestamp": "2024-01-15"})
save_pretty({"message": "Привет, мир!", "status": "success"})


# Working with URL 
def build_url(base_url, path, params=None, fragment=""):
    """Making URL with params"""
    url = base_url.rstrip('/') + '/' + path.lstrip('/')
    if params:
        url += '?' + urllib.parse.urlencode(params)
    if fragment:
        url += '#' + fragment
    return url 

api_base = "https://api.example.com"
get_user = partial(build_url, api_base)
get_posts = partial(build_url, api_base)

print(f"\n User URL: {get_user('user/123')}")
print(f"Posts with params: {get_posts("posts", params={"limit": 10, "offset": 0})}")
print(f"Post with fragment: {get_posts('posts/456', fragment='comments')}")


# Working with lists
def filter_and_transform(data, filter_func, transform_func):
    """Filtering and transform data"""
    return [transform_func(x) for x in data if filter_func(x)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Make special funcs
get_even_squares = partial(
    filter_and_transform,
    filter_func=lambda x: x %2 == 0,
    transform_func=lambda x: x ** 2,
)

get_odd_cubes = partial(
    filter_and_transform, 
    filter_func=lambda x : x %2 != 0,
    transform_func=lambda x: x ** 3
)

print(f"\nЧетные числа в квадрате: {get_even_squares(numbers)}")
print(f"Нечетные числа в кубе: {get_odd_cubes(numbers)}")