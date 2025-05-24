from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[Array]

    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    """

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = list()
        for i in range(0, n):
            new_nums.extend([nums[i], nums[i + n]])
        return new_nums
