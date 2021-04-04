import math, sys, random
from numpy import log as ln
from numpy import int32

# matrix with k rows and b columns
A = [0x21ae4036, 0x32435171, 0xac3338cf, 0xea97b40c, 0x0e504b22,
     0x9ff9a4ef, 0x111d014d, 0x934f3787, 0x6cd079bf, 0x69db5c31,
     0xdf3c28ed, 0x40daf2ad, 0x82a5891c, 0x4659c7b0, 0x73dc0ca8,
     0xdad3aca2, 0x00c74c7e, 0x9a2521e2, 0xf38eb6aa, 0x64711ab6,
     0x5823150a, 0xd13a3a9a, 0x30a5aa04, 0x0fb9a1da, 0xef785119,
     0xc9f0b067, 0x1e7dde42, 0xdda4a7b2, 0x1a1c2640, 0x297c0633,
     0x744edb48, 0x19adce93]

# matrix with k rows and b columns
# A =["00100001101011100100000000110110",
#     "00110010010000110101000101110001",
#     "10101100001100110011100011001111",
#     "11101010100101111011010000001100",
#     "00001110010100000100101100100010",
#     "10011111111110011010010011101111",
#     "00010001000111010000000101001101",
#     "10010011010011110011011110000111",
#     "01101100110100000111100110111111",
#     "01101001110110110101110000110001",
#     "11011111001111000010100011101101",
#     "01000000110110101111001010101101",
#     "10000010101001011000100100011100",
#     "01000110010110011100011110110000",
#     "01110011110111000000110010101000",
#     "11011010110100111010110010100010",
#     "00000000110001110100110001111110",
#     "10011010001001010010000111100010",
#     "11110011100011101011011010101010",
#     "01100100011100010001101010110110",
#     "01011000001000110001010100001010",
#     "11010001001110100011101010011010",
#     "00110000101001011010101000000100",
#     "00001111101110011010000111011010",
#     "11101111011110000101000100011001",
#     "11001001111100001011000001100111",
#     "00011110011111011101111001000010",
#     "11011101101001001010011110110010",
#     "00011010000111000010011001000000",
#     "00101001011111000000011000110011",
#     "01110100010011101101101101001000",
#     "00011001101011011100111010010011"]



def f(x, m):
    if m < 258:
        return ((x*0xbc164501) & 0x7fffffff) >> 23 % m 
    if m < 1024:
        return ((x*0xbc164501) & 0x7fffffff) >> 22 % m
    else:
        return ((x*0xbc164501) & 0x7fffffff) >> 22

def h(x : int32) -> int32:

    return "".join(map(str, [A[i] & x % 2 for i in range(len(A))]))
    # return "".join(map(str, [bin(A[i] & x).count("1") % 2 for i in range(len(A))]))

def rho(x):
    return x.find("1") + 1

def hyperloglog(m, k, n):

    """ 
    Estimate the number of distinct integers in a sequence of integers of len n, using an array M of m integers,
    where m is a power of 2 with m much smaller than n. 
    """
        
    M = [0 for _ in range(m)]

    for i in range(1, len(n)):

        j = f(n[i], m) # f maps integers to numbers in {0, ..., m - 1} 
        M[j] = max(M[j], rho(h(n[i]))) # h maps integers to k-bit numbers, rho identifes the left-most 1 in the bin(integer).


    Z = 1/(sum([2**(-M[ele]) for ele in M]))

    V = len([i for i in M if i == 0])

    E = m*m*Z*0.7213/(1 + 1.079/m)

    if (E < 2.5*m and V > 0):
        E = m * ln(m/V)

    return E

# USED FOR CODEJUDGE
#treshhold = int(sys.stdin.readline())

n = [int(i) for i in sys.stdin.readlines()]
#n = range(10**6, 2 * 10**6 - 1)# range(1, 100)
m = 256
k = 32

print(hyperloglog(m, k, n))

# USED FOR CODEJUDGE
# if hyperloglog(m, k, n) > treshhold:
#     print("above")
# else:
#     print("below")