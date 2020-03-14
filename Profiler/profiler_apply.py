import time
import profiler
from profiler import deco_profiler


@deco_profiler
def func_a(para1):
    time.sleep(1)
    # print(func_a.__name__, vars())

    return para1


@deco_profiler
def func_b():
    time.sleep(1)
    func_a(2)


@deco_profiler
def func_c():
    time.sleep(1)
    func_b()


def main():
    func_c()
    profiler.func_dump_trc_evt()


if __name__ == "__main__":
    main()


