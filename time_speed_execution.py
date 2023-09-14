from functools import wraps
from time import perf_counter


def time_speed(func):
    wraps(func)
    def inner(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        finish = perf_counter()
        print(f"[+] Execution time ~ {finish - start:.2f}")
        return res
    return inner
