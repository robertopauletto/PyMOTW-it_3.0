# futures_process_pool_broken.py

from concurrent import futures
import os
import signal


with futures.ProcessPoolExecutor(max_workers=2) as ex:
    print('si ottiene il pid per un esecutore')
    f1 = ex.submit(os.getpid)
    pid1 = f1.result()

    print('uccisione del processo {}'.format(pid1))
    os.kill(pid1, signal.SIGHUP)

    print('sottomissione di un altro processo')
    f2 = ex.submit(os.getpid)
    try:
        pid2 = f2.result()
    except futures.process.BrokenProcessPool as e:
        print('non è possibile far partire nuovi compiti: {}'.format(e))
