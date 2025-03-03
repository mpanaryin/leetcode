from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        An n-bit gray code sequence is a sequence of 2n integers where:

        Every integer is in the inclusive range [0, 2n - 1],
        The first integer is 0,
        An integer appears no more than once in the sequence,
        The binary representation of every pair of adjacent integers differs by exactly one bit, and
        The binary representation of the first and last integers differs by exactly one bit.
        Given an integer n, return any valid n-bit gray code sequence.

        n = 1:
        0 0
        1 0+2^0 <-- i=0

        n = 2:
        00 0
        01 1
        11 1+2^1 <-- i=1
        10 0+2^1

        n = 3:
        000 0
        001 1
        011 3
        010 2
        110 2+2^2 <-- i=2
        111 3+2^2
        101 1+2^2
        100 0+2^2
        """
        result = [0]
        for i in range(n):
            result += [(x | 1 << i) for x in reversed(result)]
        return result

s = Solution()
print(s.grayCode(2))
