import time

N = 100000


@profile
def sum_lists_comp():
    tic = time.perf_counter_ns()
    x = sum([x * x for x in range(N)])
    toc = time.perf_counter_ns()
    print(f"The time with list comprehensions is {toc - tic:0.4f} nanoseconds.")


@profile
def sum_generators():
    tic = time.perf_counter_ns()
    x = sum((x * x for x in range(N)))
    toc = time.perf_counter_ns()
    print(f"The time with generators is {toc - tic:0.4f} nanoseconds.")


sum_lists_comp()

sum_generators()