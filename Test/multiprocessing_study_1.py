import multiprocessing as mp
import time

val = 1000000
List_of_processes=[]
core_num = mp.cpu_count()
runs = 10

def fun_A( val ):
    for i in range(val):
        data = i**2+i**3+i**3
    print('fun_A done and data =', data)


if __name__ == '__main__':
    st = time.time()

    for run in range(runs):
        p = mp.Process(target=fun_A, args=(val,))
        List_of_processes.append(p)

    for p in List_of_processes:
        p.start()
        print('start()',p, 'core num. =',core_num)

    for p in List_of_processes:
        print('join()', p, 'start', p.is_alive())
        p.join()
        print('join()',p, 'end', p.is_alive())

    et = time.time()
    duration = round(et - st, 3)
    print('\nduration =', duration, ', core num. =',core_num,'\n')



