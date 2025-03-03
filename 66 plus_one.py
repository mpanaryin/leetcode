from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        You are given a large integer represented as an integer array digits,
        where each digits[i] is the ith digit of the integer.
        The digits are ordered from most significant to least significant in left-to-right order.
        The large integer does not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.
        """
        int_result = int(''.join([str(digit) for digit in digits])) + 1
        return [int(digit) for digit in str(int_result)]

digits = [1,2,3]
s = Solution()
result = s.plusOne(digits)
print(result)
