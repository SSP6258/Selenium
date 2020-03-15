import time
import logging
import json
import os
import threading


dict_of_trc_evt = {'traceEvents': []}


def func_form_trc_evt(name, ts, te, dur):
    dict_of_trc = {"cat": "function",
                   "name": name,
                   "ts": ts,
                   "dur": dur,
                   "tid": 1,
                   "pid": 1,
                   "ph": "X"}

    dict_of_trc_evt['traceEvents'].append(dict_of_trc)


def func_create_logger():
    log_file = 'profiler.log'
    log_fmt = "%(levelname)s, %(asctime)s,  %(message)s"

    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format=log_fmt,
                        filemode="w")

    return logging.getLogger()


def deco_profiler(func):

    logger = func_create_logger()
    
    def wrapper(*args, **kwargs):
        name = str(func.__name__)
        logger.info(name + " start")
        ts = time.time()*1e6  # us
        # ==========================
        result = func(*args, **kwargs)
        # ==========================
        te = time.time()*1e6  # us
        dur = te - ts
        pid = os.getpid()
        tid = threading.current_thread()
        logger.info(name + " takes: "+str(round(dur/1e3, 0))+" ms, pid = "+str(pid)+", tid = "+str(tid))
        func_form_trc_evt(name, ts, te, dur)

        return result
        
    return wrapper


def func_dump_trc_evt():

    # print(dict_of_trc_evt)

    with open('profiler_TrcEvt.json', 'w', encoding='utf-8') as file:
        json.dump(dict_of_trc_evt, file, indent=2)