# multiprocessing_names.py

import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, 'In partenza')
    time.sleep(2)
    print(name, 'In uscita')


def my_service():
    name = multiprocessing.current_process().name
    print(name, 'In partenza')
    time.sleep(3)
    print(name, 'In uscita')


if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )
    worker_1 = multiprocessing.Process(
        name='Elaboratore 1',
        target=worker,
    )
    worker_2 = multiprocessing.Process(  # nome predefinito
        target=worker,
    )

    worker_1.start()
    worker_2.start()
    service.start()