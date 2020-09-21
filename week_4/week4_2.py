from numpy import array, hstack, vstack, array2string, int32, zeros
import sys

# use np.fromstring('1 2', dtype=int, sep=' ')
n = sys.stdin.readline()
a = array([array([int(i) for i in sys.stdin.readline().strip("\n").split()]) for _ in range(int(n))])
blank = sys.stdin.readline() # middle line
b = array([array([int(i) for i in sys.stdin.readline().strip("\n").split()]) for _ in range(int(n))])

def partition(array, n):
    p = int(n / 2)
    return array[:p, :p], array[p:, :p], array[:p, p:], array[p:, p:]

def square_matrix_mul_rec(A, B):
    
    if isinstance(A, int32): n = 1
    else: n = A.shape[0]

    if n == 1:
        c_00 = A * B

    elif n == 2:
        a_00, a_10, a_01, a_11 = partition(A, n)
        b_00, b_10, b_01, b_11 = partition(B, n)

        c_00 = square_matrix_mul_rec(a_00, b_00) - \
                  square_matrix_mul_rec(a_01, b_10)

        c_01 = square_matrix_mul_rec(a_00, b_01) - \
                  square_matrix_mul_rec(a_01, b_11)

        c_10 = square_matrix_mul_rec(a_10, b_00) - \
                  square_matrix_mul_rec(a_11, b_10)

        c_11 = square_matrix_mul_rec(a_10, b_01) - \
                  square_matrix_mul_rec(a_11, b_11)

    else:

        a_00, a_10, a_01, a_11 = partition(A, n)
        b_00, b_10, b_01, b_11 = partition(B, n)


        c_00 = square_matrix_mul_rec(a_00, b_00) + \
                  square_matrix_mul_rec(a_01, b_10)

        c_01 = square_matrix_mul_rec(a_00, b_01) + \
                  square_matrix_mul_rec(a_01, b_11)

        c_10 = square_matrix_mul_rec(a_10, b_00) + \
                  square_matrix_mul_rec(a_11, b_10)

        c_11 = square_matrix_mul_rec(a_10, b_01) + \
                  square_matrix_mul_rec(a_11, b_11)

    if n == 1: return c_00
    return vstack([hstack([c_00, c_01]), hstack([c_10, c_11])])


for row in square_matrix_mul_rec(a, b):
    print(array2string(row, separator=' ')[1:-1].lstrip(" "))


