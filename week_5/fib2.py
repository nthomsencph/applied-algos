import sys
import time

x = dict()

def fib(n):

    if n < 2:
        return 1
    
    if not (n in x):
        x[n] =  fib(n - 1) + fib(n - 2)

    return x[n]


t0 = time.time()

print(round(fib(int(sys.argv[1])), 6), round(time.time() - t0, 5))