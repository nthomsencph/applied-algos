from numpy import array, array2string, fromstring, int32
from sys import stdin, stdout

def ClassicQuicksort(A : array, left : int, right : int):

    """ class quicksort algorithm. Sorts A in place. """

    if right - left < 1: return

    p = A[right]
    i, j = left - 1, right

    while True: # py do-while look..

        i += 1
        while j > i and A[i] < p:
            i += 1

        j -= 1
        while j > i and A[j] > p:
            j -= 1

        if j > i:
            
            A[i], A[j] = A[j], A[i]

        else:
            
            A[right], A[i] = A[i], A[right]

            ClassicQuicksort(A, left, i - 1)
            ClassicQuicksort(A, i + 1, right)

            return

if __name__ == "__main__":

    # needed to unwrap from and rewrap in string
    A = fromstring(stdin.readline(), dtype = int32, sep = " ")
    ClassicQuicksort(A, 0, len(A) - 1)
    stdout.write(array2string(A)[1:-1])

    # test data
    # A = array([12,3939, 58, 124, 97, 66, 41, 21, 125, 993, 2, 27, 31, 11, 848, 33, 16, 99, 69, 420])
    # B = array([12,3939, 58, 124, 97, 66, 41, 21, 125, 993, 2, 27, 31, 11, 848, 33, 16, 99, 69, 420])

    # driver code
    # ThreePivotQuicksort(A, 0, len(A) - 1)
    # print(A)
    # print(sorted(B))