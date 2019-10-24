import multiprocessing as mp
import time


def fun_A( val ):
    for i in range(val):
        data = i**2+i**3+i**3
    print('fun_A done and data =', data)


def fun_B( val ):
    for i in range(val):
        data = i**2+i**3+i**3

    print('fun_B done and data =', data)



val = 10000000

if __name__ == '__main__':
    st = time.time()
    if False:
        fun_A(val)
        fun_B(val)
    else:
        p1 = mp.Process(target=fun_A, args=(val,))
        p2 = mp.Process(target=fun_B, args=(val,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    et = time.time()
    duration = round(et - st, 3)
    core_num = mp.cpu_count()
    print('duration =', duration, ', core num. =',core_num)



