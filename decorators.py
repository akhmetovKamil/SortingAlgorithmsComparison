from typing import Callable
import time
import copy
def iterations(iter_count: int):
    def wrapper(func: Callable):
        def inner_wrapper(arr: list):
            total_time = 0
            for _ in range(iter_count):
                start_time = time.perf_counter_ns()
                new_arr = copy.deepcopy(arr)
                func(new_arr)
                end_time = time.perf_counter_ns()
                total_time += end_time - start_time
            return total_time/iter_count
        return inner_wrapper
    return wrapper

iterations_10 = iterations(iter_count=10)
iterations_50 = iterations(iter_count=50)
