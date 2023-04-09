import threading
import math
import time

def calculate_sqrt(num):
    result = math.sqrt(num)
    print(f"Square root of {num}: {result}")

if __name__ == "__main__":
    nums = [25, 36, 49, 64, 81, 100]
    threads = []
    start_time = time.time()
    for num in nums:
        thread = threading.Thread(target=calculate_sqrt, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")