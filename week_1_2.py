import sys
from numpy import dot, array


n, k = sys.stdin.readline().strip("\n").split()
v = array([array([int(i) for i in sys.stdin.readline().strip("\n").split()]) for _ in range(int(k))])
blank = sys.stdin.readline() # middle line
w = array([array([int(i) for i in sys.stdin.readline().strip("\n").split()]) for _ in range(int(k))])


def inner(n, v, w):
    for v_i in v:
        for w_i in w:
            if dot(v_i, w_i) == 0:
                return "yes"

    return "no"

print(inner(n, v, w))
            
