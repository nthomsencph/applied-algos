import sys
import time

def fib(n):

    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)

t0 = time.time()

print(round(fib(int(sys.argv[1])), 6), round(time.time() - t0, 5))