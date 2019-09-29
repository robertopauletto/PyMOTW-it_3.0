# multiprocessing_condition.py

import multiprocessing
import time


def stage_1(cond):
    """esegue il primo segmento del lavoro
    poi notifica al secondo segmento stage_2 di continuare
    """
    name = multiprocessing.current_process().name
    print('In partenza', name)
    with cond:
        print('{} finito e pronto per il secondo segmento'.format(name))
        cond.notify_all()


def stage_2(cond):
    """attende la condizione che dice che stage_1 è completato"""
    name = multiprocessing.current_process().name
    print('In partenza', name)
    with cond:
        cond.wait()
        print('{} in esecuzione'.format(name))


if __name__ == '__main__':
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name='s1',
                                 target=stage_1,
                                 args=(condition,))
    s2_clients = [
        multiprocessing.Process(
            name='stage_2[{}]'.format(i),
            target=stage_2,
            args=(condition,),
        )
        for i in range(1, 3)
    ]

    for c in s2_clients:
        c.start()
        time.sleep(1)
    s1.start()

    s1.join()
    for c in s2_clients:
        c.join()
