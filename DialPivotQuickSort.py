from numpy import array2string, fromstring, int32
from sys import stdin, stdout
from secrets import choice

def TwoPivotQuicksort(A, left, right):

    if right - left < 1: return

    p = choice(range(right))
    q = choice(range(right))

    if A[p] > A[q]:

        q, p = p, q

    k = l = left + 1
    g = right - 1

    while k <= g:

        if A[k] < A[p]:
            
            A[k], A[l] = A[l], A[k]
            l += 1

        elif A[k] >= A[q]:

            while A[g] > A[q] and k < g:

                g -= 1

            A[k], A[g] = A[g], A[k]
            g -= 1

            if A[k] < A[p]:

                A[k], A[l] = A[l], A[k]
                l += 1

        k += 1
    
    l -= 1
    g += 1

    A[left], A[l] = A[l], A[left]
    A[right], A[g] = A[g], A[right]

    TwoPivotQuicksort(A, left, l - 1) 
    TwoPivotQuicksort(A, l + 1, g - 1) 
    TwoPivotQuicksort(A, g + 1, right) 

if __name__ == "__main__":

    A = fromstring(stdin.readline(), dtype = int32, sep = " ")
    TwoPivotQuicksort(A, 0, len(A) - 1)
    stdout.write(array2string(A)[1:-1])

