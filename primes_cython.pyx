def primes(int number_of_primes):
    cdef int n, i, len_primes
    cdef int primes[1000]

    if number_of_primes > 1000:
        number_of_primes = 1000

    len_primes = 0
    n = 2
    while len_primes < number_of_primes:
        for i in primes[:len_primes]:
            print(i)
            if n % i == 0:
                break
        else:
            primes[len_primes] = n
            len_primes += 1
        n += 1

    result_as_list = [prime for prime in primes[:len_primes]]
    return result_as_list

if __name__ == '__main__':
    result_as_list = primes(20)
    print(result_as_list)
