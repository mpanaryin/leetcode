import itertools


class Solution:
    """
    Grade [Easy]

    You are given an array of digits called digits.
    Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

    Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

    Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
    """
    def totalNumbers(self, digits: list[int]) -> int:
        counter = 0
        nums = set(itertools.permutations(digits, 3))
        for str_num in nums:
            num = int(''.join([str(i) for i in str_num]))
            if num % 2 == 0 and num // 100 >= 1:
                counter += 1
        return counter
