import random
import multiprocessing
import time

def monte_carlo_pi(n, queue):
    inside_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / n
    queue.put(pi_estimate)

if __name__ == '__main__':
    processes = []
    queue = multiprocessing.Queue()
    start_time = time.time()
    for i in range(4):
        p = multiprocessing.Process(target=monte_carlo_pi, args=(2500000, queue))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    pi_estimate = sum([queue.get() for i in range(4)]) / 4

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time}")
    print(f"Estimated value of pi: {pi_estimate}")
