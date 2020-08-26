from numpy.random import randint
from sys import stdin, stdout

n, k = stdin.readline().strip("\n").split()

stdout.write(f"{n} {k}\n")
[stdout.write(f"{' '.join(map(str, randint(2, size= int(n)) ))}\n") for _ in range(int(k))]
stdout.write("\n")
[stdout.write(f"{' '.join(map(str, randint(2, size= int(n)) ))}\n") for _ in range(int(k))]

# to be used in linux pipe from terminal, e.g. "python3 week_1_3.py | python3 week_1_2.py"