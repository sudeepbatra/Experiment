from multiprocessing import Value, Process


# Compare to increment_shared_counter_parallel
def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()
    shared_int.value = shared_int.value + 1
    shared_int.get_lock().release()


def increment_value_with_block(shared_int: Value):
    with shared_int.get_lock():
        shared_int.value = shared_int.value + 1


if __name__ == '__main__':
    for i in range(10000000):
        integer = Value("i", 0)
        procs = [Process(target=increment_value_with_block, args=(integer,)),
                 Process(target=increment_value_with_block, args=(integer,)),
                 Process(target=increment_value_with_block, args=(integer,)),
                 Process(target=increment_value_with_block, args=(integer,))]
        [p.start() for p in procs]
        [p.join() for p in procs]
        print(integer.value)
        # Race Condition
        assert (integer.value == 4)
