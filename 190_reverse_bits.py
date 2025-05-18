class Solution:
    """
    Grade[Medium]
    Topics[Divide and Conquer, Bit Manipulation]

    Reverse bits of a given 32 bits unsigned integer.

    Note:

    Note that in some languages, such as Java, there is no unsigned integer type. In this case,
    both input and output will be given as a signed integer type. They should not affect your implementation,
    as the integer's internal binary representation is the same, whether it is signed or unsigned.

    In Java, the compiler represents the signed integers using 2's complement notation. Therefore,
    in Example 2 above, the input represents the signed integer -3 and
    the output represents the signed integer -1073741825.
    """

    def reverseBits(self, n: int) -> int:
        """
        Reverse bits of a given 32 bits unsigned integer.
        """
        reversed_n = bin(n)[2:][::-1]
        if len(reversed_n) != 32:
            reversed_n = reversed_n + "0" * (32 - len(reversed_n))
        return int(reversed_n, 2)

    def reverseBits2(self, n: int):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans


n = 43261596
s = Solution()
result = s.reverseBits2(n)
print(result)
