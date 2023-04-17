"""Example of context managers using the 'with' statement"""

import requests

# requests.Session() is the context manager
with requests.Session() as session:

    # Subscribe?
    response = session.get('https://www.youtube.com/channel/UCUT7HRJyKHFG-jPMopUfcBA')
    print(response.text)

# open() is the context manager
with open('example.txt', 'w') as file_handle:
    file_handle.write('Hello, world!')