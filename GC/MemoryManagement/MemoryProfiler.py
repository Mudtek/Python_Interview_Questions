"""Example of using the memory_profiler"""

# To run:
#
# mprof run MemoryProfiler.py
# mprof plot

import numpy as np
from memory_profiler import profile

@profile
def run_experiment(n):
    data = np.random.random((n, n))
    m = np.sum(data)
    del data
    return m

if __name__ == '__main__':
    run_experiment(1000)