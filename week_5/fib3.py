import sys
import time

def fib(n):

    if n < 2:
        return 1

    b = 1
    a = 1

    for _ in range(n - 1):
        x = a + b
        a = b
        b = x
    
    return x


t0 = time.time()

print(round(fib(int(sys.argv[1])), 6), round(time.time() - t0, 5))