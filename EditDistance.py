from numpy import int32, zeros
from sys import argv
import math

def editDist(source, target):

    if source == target: # base case
        return 0

    source = ["#"] + list(source) #[k for k in source]
    target = ["#"] + list(target) # [k for k in target]

    m, n = len(source), len(target)

    sol = zeros((m, n), dtype = int32)

    sol[0] = [j for j in range(n)]
    sol[:, 0] = [j for j in range(m)]

    if target[1] != source[1]:

        sol[1, 1] = 2 

    for c in range(1, n):

        for r in range(1, m):

            if target[c] != source[r]:

                sol[r, c] = min(sol[r - 1, c], 
                                sol[r - 1, c - 1], 
                                sol[r, c - 1]) + 1

            else:
                
                sol[r, c] = sol[r - 1, c - 1]

    # print(sol)
    return sol[-1, -1]

import time

s = time.time()

print(editDist("aadfaaaadfaaaadfaaaadfaaaadfaa",  "aadfaaaadfaaaadfaaaadfaaaadfaa"))

print(round(time.time() - s, 4))
# print(editDist(argv[1], argv[2]))

import Levenshtein as lev
s = time.time()

print(lev.distance("aadfaaaadfaaaadfaaaadfaaaadfaa",  "aadfaaaadfaaaadfaaaadfaaaadfaa"))

print(round(time.time() - s, 4))
