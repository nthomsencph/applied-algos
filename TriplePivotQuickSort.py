
from numpy import array2string, fromstring, insert, int32, array
from sys import stdin, stdout


# def InsertionSort(A : array, left : int, right : int) -> None:

#     """ insertion sort to handle smaller subarrays for the structure. WIP  """

#     for i in range(left, right):

#         e = A[i]
#         pos = i

#         while pos > 0 and A[pos - 1] > e:

#             A[pos] = A[pos -1]
#             pos = pos - 1

#         A[pos] = e


def PivotSwaps(A : array, left : int, right : int):

    """ we need to make sure that p < q < r """

    if A[left] > A[left + 1]:

        A[left], A[left + 1] = A[left + 1], A[left]

    if A[left] > A[right]:

        A[left], A[left + 1] = A[left + 1], A[left]
        A[left], A[right] = A[right], A[left]

    elif A[left + 1] > A[right]:

        A[left + 1], A[right] = A[right], A[left + 1]
        

def swap(A : array, a : int, b : int):

    """ to clean up main algo. Simply swaps elements in A """

    A[a], A[b] = A[b], A[a]

def ThreePivotQuickSort(A : array, left : int, right : int): 

    """ wrapper for three pivot sorting algorithm """

    # if left + 10 > right: 
    #     insertSort(A, left, right)
    #     return

    if left < right:

        lp, qp, rp = partition(A, left, right) 
        ThreePivotQuickSort(A, left, lp - 1) 
        ThreePivotQuickSort(A, lp, qp - 1) 
        ThreePivotQuickSort(A, qp, rp - 1) 
        ThreePivotQuickSort(A, rp, right) 
            
def partition(A : array, left : int, right : int): 

    """ partition function for three pivot sorting algorithm as per Kushagra, López-Ortiz, Munro & Qiao (2014).
        sorts A in place. """
        
    a = b = left + 2
    c = d = right - 1

    PivotSwaps(A, left, right)

    p = A[left]
    q = A[left + 1]
    r = A[right]

    while b <= c:

        while A[b] < q and b <= c:

            if A[b] < p:

                swap(A, a, b)
                a += 1

            b += 1
        
        while A[c] > q and b <= c:

            if A[c] > r:

                swap(A, c, d)
                d -= 1

            c -= 1

        if b <= c:

            if A[b] > r:

                if A[c] < p and b <= c:

                    swap(A, b, a)
                    swap(A, c, a)
                    a += 1

                else:

                    swap(A, b, c)

                swap(A, d, c)
                b += 1
                c -= 1
                d -= 1

            else:

                if A[c] < p and b <= c:

                    swap(A, b, a)
                    swap(A, a, c)
                    a += 1

                else:

                    swap(A, b, c)

                b += 1
                c -= 1

    a -= 1
    b -= 1
    c += 1
    d += 1

    swap(A, left + 1, a)
    swap(A, a, b)
    a -= 1

    swap(A, left, a)
    swap(A, right, d)

    return b, c, d,  
  

if __name__ == "__main__":
    
    # needed to unwrap from and rewrap in string
    A = fromstring(stdin.readline(), dtype = int32, sep = " ")
    ThreePivotQuickSort(A, 0, len(A) - 1)
    stdout.write(array2string(A)[1:-1])
      
    # test data  
    # A = [642764618,1427345980,1362150343,97390251,984486706,1183584717,1551419636,1023431820,1389878077,1682819471,217247008]
    # B = A

    # driver code
    # ThreePivotQuickSort(A, 0, len(A) - 1)
    # print(A[0:20])
    # print(sorted(B)[0:20])
