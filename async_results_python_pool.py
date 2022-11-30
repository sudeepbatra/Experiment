from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__t":
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=("Jeff",))
        hi_john = process_pool.apply_async(say_hello, args=("John",))
        print(hi_jeff.get())
        print(hi_john.get())
