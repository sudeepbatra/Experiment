import time

# Implementation uses recursion and is overall a relatively slow algorithm requiring exponential O(2^N) time to complete.
def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) is {fib(number)}')


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start = time.time()
fibs_no_threading()
end = time.time()
print(f"Completed in {end - start:.4f} seconds")
