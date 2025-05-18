from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[Array, Math]

    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer.
    The digits are ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        int_result = int(''.join([str(digit) for digit in digits])) + 1
        return [int(digit) for digit in str(int_result)]

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(digits)
        for i in reversed(range(n)):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


digits = [1, 2, 3]
s = Solution()
result = s.plusOne(digits)
print(result)
