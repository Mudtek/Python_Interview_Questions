import random
import time

def monte_carlo_pi(n):
    inside_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / n
    return pi_estimate

if __name__ == '__main__':
    start_time = time.time()
    pi_estimate = monte_carlo_pi(10000000)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time}")
    print(f"Estimated value of pi: {pi_estimate}")
