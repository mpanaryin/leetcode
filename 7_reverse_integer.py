class Solution:
    """
    Grade[Medium]
    Topics[Math]

    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    def reverse(self, x: int) -> int:
        """
        Time complexity: O(log₁₀ n)
        Space complexity: O(log₁₀ n)
        """
        if x < 0:
            x = x * (-1)
            negative = -1
        else:
            negative = 1

        str_x = str(x)[::-1]
        for ind, x in enumerate(str_x):
            if x != '0':
                result = int(str_x[ind:]) * negative
                if result < -2**31 or result > 2**31:
                    return 0
                return result
        return 0
