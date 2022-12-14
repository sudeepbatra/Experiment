from multiprocessing import Value, Process


def increment_value(shared_int: Value):
    shared_int.value += 1


if __name__ == '__main__':
    for i in range(10000000):
        integer = Value("i", 0)
        procs = [Process(target=increment_value, args=(integer,)), Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)), Process(target=increment_value, args=(integer,))]
        [p.start() for p in procs]
        [p.join() for p in procs]
        print(integer.value)
        # Race Condition
        assert (integer.value == 4)
