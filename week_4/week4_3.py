# Freivalds’ Algorithm

# Compute P⃗ = A × (Br)⃗ – Cr⃗.
# Return true if P⃗ = ( 0, 0, …, 0 )T, return false otherwise.

from numpy import array, fromstring
import sys

n = int(sys.stdin.readline())

A = array([fromstring(sys.stdin.readline(), dtype = int, sep = " ") for _ in range(n)]) # matrix A
sys.stdin.readline() # middle line

B = array([fromstring(sys.stdin.readline(), dtype = int, sep = " ") for _ in range(n)]) # matrix B
sys.stdin.readline() # middle line

C = array([fromstring(sys.stdin.readline(), dtype = int, sep = " ") for _ in range(n)]) # matrix C
sys.stdin.readline() # middle line

x = array([fromstring(sys.stdin.readline(), dtype = int, sep = " ") for _ in range(3)]) # 3 test vectors

def freivals_algo(A, B, C, x, n):

    """ Evaluates (ABx == Cx) in single iteration w/ 
    probability 1/2. Error probability decreases expontentially such that
    prob(err) <= 2^(-z), where z is number of iterations.

    Returns:
        str: faulty (negative) or correct (positive)
    """

    ABx, Bx, Cx = [0] * n, [0] * n, [0] * n # base values

    # populate Bx
    for i in range(n):
        for j in range(n):
            Bx[i] += B[i][j] * x[j]

    # populate ABx
    for i in range(n):
        for j in range(n):
            ABx[i] += A[i][j] * Bx[j] 

    # populate Cx
    for i in range(n):
        for j in range(n):
            Cx[i] += C[i][j] * x[j]

    # check if ABx == Cx
    for i in range(n):
        if ABx[i] - Cx[i] != 0:
            return "faulty"

    return "correct"


for vec in x: print(freivals_algo(A, B, C, vec, n))



