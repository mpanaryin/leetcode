class Solution:
    """
    Grade[Medium]
    Topics[Math, String, Bit Manipulation, Simulation]

    Given two binary strings a and b, return their sum as a binary string.
    """
    def add_binary(self, a: str, b: str) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        max_len = max(len(a), len(b))
        num1 = a.zfill(max_len)[::-1]
        num2 = b.zfill(max_len)[::-1]
        additional = 0
        new_num = ''
        for i in zip(num1, num2):
            digit1 = int(i[0]) + additional
            digit2 = int(i[1])
            additional = (digit1 + digit2) // 2
            new_num += str((digit1 + digit2) % 2)
        if additional:
            new_num += '1'
        return new_num[::-1]
