"""Test the speed of this multithreading vs the linear non-threading list of requests"""

import requests
import threading
import time

urls = [
    'https://www.amazon.com',
    'https://www.google.com',
    'https://www.facebook.com',
    'https://www.hp.com',
    'https://www.dell.com',
    'https://www.reddit.com',
    'https://www.youtube.com',
    'https://www.instagram.com',
    'https://www.github.com',
    'https://www.aws.com',
]

def get_body(url: str) -> None:
    try:
        response = requests.get(url)
        body_info = response.text[:50].replace('\n', ' ').replace('\r', '')
        print(f"{url}: {body_info}")
    except:
        print(f"Error fetching body for {url}")


if __name__ == '__main__':
    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=get_body, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")
