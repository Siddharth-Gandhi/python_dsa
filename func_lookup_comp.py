import time


def normal():
    tic = time.perf_counter_ns()
    ls = ["a", "5", "b", "adf"]
    for i in ls:
        print(len(i))
    toc = time.perf_counter_ns()
    return toc - tic


def abnormal():
    tic = time.perf_counter_ns()
    ls = ["a", "5", "b", "adf"]
    fn = len
    for i in ls:
        print(fn(i))
    toc = time.perf_counter_ns()
    return toc - tic


normal_sum = 0
abnormal_sum = 0
N = 1000
for i in range(N):
    normal_sum += normal()

for i in range(N):
    abnormal_sum += abnormal()

print("For 1000 runs:")
print("Average time for normal len is", normal_sum / N, "nanoseconds")
print("Average time for locally stored len is", abnormal_sum / N, "nanoseconds")