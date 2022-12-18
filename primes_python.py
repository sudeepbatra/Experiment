import cython


def primes(number_of_primes: cython.int):
    i: cython.int
    primes_array: cython.int[1000]

    if number_of_primes > 1000:
        number_of_primes = 1000

    if not cython.compiled:
        primes_array = [0] * 1000

    len_primes: cython.int = 0
    n: cython.int = 2

    # Loop statements may have an else clause; it is executed when the loop terminates
    # through exhaustion of the iterable (with for) or when the condition becomes false (with while),
    # but not when the loop is terminated by a break statement.
    while len_primes < number_of_primes:
        for i in primes_array[:len_primes]:
            if n % i == 0:
                break
        else:
            primes_array[len_primes] = n
            len_primes += 1
        n += 1

    result_as_list = [prime for prime in primes_array[:len_primes]]
    return result_as_list


if __name__ == '__main__':
    result_as_list = primes(20)
    print(result_as_list)
