import math
import time

def calculate_sqrt(num):
    result = math.sqrt(num)
    print(f"Square root of {num}: {result}")

if __name__ == "__main__":
    nums = [25, 36, 49, 64, 81, 100]
    start_time = time.time()
    for num in nums:
        calculate_sqrt(num)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")
