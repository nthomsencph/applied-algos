import sys
import numpy as np


n, k = sys.stdin.readline().strip("\n").split()
v = [[int(i) for i in sys.stdin.readline().strip("\n").split()] for _ in range(int(k))]
blank = sys.stdin.readline() # middle line
w = [[int(i) for i in sys.stdin.readline().strip("\n").split()] for _ in range(int(k))]

results = 0

def inner(n, v, w):
    for v_i in v:
        for w_i in w:
            if np.dot(v_i, w_i) == 0:
                return "yes"

    return "no"

print(inner(n, v, w))
            
