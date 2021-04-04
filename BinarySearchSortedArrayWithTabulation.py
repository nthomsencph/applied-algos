from sys import stdin, stdout, argv
from numpy import array, binary_repr, fromstring, int32, sort, array2string


class TabulatedSearch():

    def __init__(self, n, S, Q) -> str:

        self.n     = int32(n)
        self.k     = 10 #int32(argv[1]) # 10 

        self.S     = self.strToArr(S)
        self.table = self.initTable()

        stdout.write(self.checkQ(self.strToArr(Q)))


    @staticmethod
    def strToArr(S: array) -> array:

        return fromstring(S, dtype = int32, sep = " ")


    def initTable(self) -> array:

        return array([self.interval(i) for i in range(0, 2 ** self.k)])


    def toggleBits(self, i: int32) -> int32:

        return (i << (32 - self.k)) ^ (2 ** (32 - self.k) - 1)


    def shiftBits(self, i: int32) -> int32:

        return i << (32 - self.k)


    def firstK(self, i: int32) -> int32:

        return int(binary_repr(i, width = 32)[:self.k], 2)


    def interval(self, i : int32) -> tuple:

        return (max(self.predInterval(self.shiftBits(i)), 0), self.predInterval(self.toggleBits(i)))


    def predInterval(self, q : int32) -> int32:

        return self._pred(q, 0, self.n) if self.S[-1] > q  else self.n - 1


    def checkQ(self, Q: array) -> str:

        return array2string(array([self.predQs(q) for q in Q]))[1:-1]


    def predQs(self, q : int32) -> int32 or None:

        return self.S[self._pred(q, *self.table[self.firstK(q)])] if self.S[0] <= q else None


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

    TabulatedSearch("10",
            "11 19 4 3 7 8 10 20 9 1",
            "14 20 0 12 11 13 8 19 9 3")           

    # TabulatedSearch(stdin.readline(), # n
    #                 stdin.readline(), # S
    #                 stdin.readline()) # q