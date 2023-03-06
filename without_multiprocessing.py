"""
whenever we are doing compute intensive operation - multi-processing
"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"[ INFO ] total time to execute :: {end}")
        return result

    return wrapper


def some_heavy_work(range_):
    return [i**2 for i in range(range_)]


@timeit
def main():
    ranges = [10001, 10002, 10003, 10004, 10005, 10006]

    for range_ in ranges:
        some_heavy_work(range_)


if __name__ == "__main__":
    main()