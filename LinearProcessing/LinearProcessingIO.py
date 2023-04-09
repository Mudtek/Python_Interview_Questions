import requests
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

start_time = time.time()
for url in urls:
    try:
        response = requests.get(url)
        body_info = response.text[:50].replace('\n', ' ').replace('\r', '')
        print(f"{url}: {body_info}")
    except:
        print(f"Error fetching body for {url}")

end_time = time.time()
total_time = end_time - start_time
print(f"Total time taken: {total_time} seconds")
