from numpy import array, matmul, array2string
import sys


n = sys.stdin.readline()
a = array([array([int(i) for i in sys.stdin.readline().strip("\n").split()]) for _ in range(int(n))])
blank = sys.stdin.readline() # middle line
b = array([array([int(i) for i in sys.stdin.readline().strip("\n").split()]) for _ in range(int(n))])

for row in matmul(a, b):
    print(array2string(row, separator=' ')[1:-1].lstrip(" "))

