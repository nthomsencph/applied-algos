import sys

n = sys.stdin.readline()
v = sys.stdin.readline()
w = sys.stdin.readline()


def inner_prod(v, w, n, result = 0):
    v, w = v.split(), w.split()
    for i in range(int(n)):
        result += int(v[i]) * int(w[i])
    return result

print(inner_prod(v, w, n))