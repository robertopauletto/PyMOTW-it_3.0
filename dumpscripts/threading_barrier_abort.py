# threading_barrier_abort.py

import threading
import time


def worker(barrier):
    print(threading.current_thread().name,
          'in attesa della barriera con altri {}'.format(
              barrier.n_waiting))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'interruzione')
    else:
        print(threading.current_thread().name, 'dopo la barriera',
              worker_id)


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name='worker-%s' % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'partenza')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()
