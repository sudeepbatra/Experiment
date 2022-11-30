import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start_time = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end_time = time.time()
    print(f"Finished counting to {count_to} in {end_time - start_time} seconds")
    return counter


if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [5000000000, 1, 3, 5, 22, 100000000, 200000000, 500000000, 1000000000]
        for result in process_pool.map(count, numbers):
            print(result)
