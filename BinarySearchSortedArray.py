from numpy import sort, array, fromstring, int32, array2string
from sys import stdin, stdout

class SortedArray():


    def __init__(self, n, S, Q) -> None:
        
        self.n = int32(n)
        self.S = self.strToArr(S)
        stdout.write(self.checkQ(self.strToArr(Q)))


    @staticmethod
    def strToArr(S : array) -> array:

        return fromstring(S, dtype = int32, sep = " ")
        

    def checkQ(self, Q : array) -> str:

        return array2string(array([self.S[self._pred(q, 0, self.n - 1)] if q >= self.S[0] else None for q in Q]))[1:-1]


    def _pred(self, q, start, end) -> int32:

        if end - start < 0:

            return end

        jmp = start + (end - start) // 2

        if self.S[jmp] == q: # if q equals

            return jmp

        elif self.S[jmp] > q:  # if q is smaller

            return self._pred(q, start, jmp - 1)

        else:  # else if q is larger

            return self._pred(q, jmp + 1, end)


if __name__ == "__main__":

    # SortedArray("10",
    #             "1986132998 1673711575 2037115399 622591254 1916486003 1781644014 179423724 36671725 1271368787 658727549",
    #             "909990628 814293600 1138355335 768970614 279823433")

    SortedArray(stdin.readline(), # n
                stdin.readline(), # S
                stdin.readline()) # q



