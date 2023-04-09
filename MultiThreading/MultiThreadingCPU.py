import random
import threading
import time

def monte_carlo_pi(n, results_list):
    inside_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / n
    results_list.append(pi_estimate)

if __name__ == '__main__':
    threads = []
    results_list = []
    start_time = time.time()
    for i in range(4):
        t = threading.Thread(target=monte_carlo_pi, args=(2500000, results_list))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    pi_estimate = sum(results_list) / 4

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time}")
    print(f"Estimated value of pi: {pi_estimate}")
