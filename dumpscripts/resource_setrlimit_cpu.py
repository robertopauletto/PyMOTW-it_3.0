# resource_setrlimit_cpu.py

import resource
import signal
import time


# Imposta un gestore di segnale per notificare
# quando il tempo si esaurisce
def time_expired(n, stack):
    print('SCADUTO :', time.ctime())
    raise SystemExit('(tempo scaduto)')


signal.signal(signal.SIGXCPU, time_expired)

# Adjust the CPU time limit
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Limite soft inizia come  :', soft)

resource.setrlimit(resource.RLIMIT_CPU, (1, hard))

soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Limite soft modificato in:', soft)
print()

# Consume some CPU time in a pointless exercise
print('Partenza:', time.ctime())
for i in range(200000):
    for i in range(200000):
        v = i * i

# We should never make it this far
print('Uscita :', time.ctime())
