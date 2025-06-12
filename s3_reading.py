from urllib.request import urlopen
import time

import os
from dotenv import load_dotenv

load_dotenv()


url = os.getenv('S3_URL')


def process_user_ids(user_ids):
    print(f"Processing batch of {len(user_ids)} users")
    # Здесь может быть любой код: запрос в Mongo, API вызов и т.д.

batch_size = 300
user_ids = []

with urlopen(url) as response:
    next(response)  # <- пропускаем первую строку с "account_id"

    for line in response:
        user_id = line.decode("utf-8").strip()
        print(user_id)
        if user_id:
            user_ids.append(user_id)

            if len(user_ids) == batch_size:
                process_user_ids(user_ids)
                user_ids = []

if user_ids:
    process_user_ids(user_ids)
