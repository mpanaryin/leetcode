class Solution:
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