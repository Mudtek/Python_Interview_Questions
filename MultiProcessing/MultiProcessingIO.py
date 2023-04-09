"""Multiprocessing example"""

import requests
import multiprocessing
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

def get_body(url):
    try:
        response = requests.get(url)
        body_info = response.text[:50].replace('\n', ' ').replace('\r', '')
        print(f"{url}: {body_info}")
    except:
        print(f"Error fetching body for {url}")

if __name__ == '__main__':
    processes = []
    start_time = time.time()
    for url in urls:
        process = multiprocessing.Process(target=get_body, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")
