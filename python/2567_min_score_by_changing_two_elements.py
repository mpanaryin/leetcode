from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[Array, Greedy, Sorting]

    You are given a 0-indexed integer array nums.

    The low score of nums is the minimum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.
    The high score of nums is the maximum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.
    The score of nums is the sum of the high and low scores of nums.
    To minimize the score of nums, we can change the value of at most two elements of nums.

    Return the minimum possible score after changing the value of at most two elements of nums.

    Note that |x| denotes the absolute value of x.

    Логика решения: максимум мы переставим два элемента.
    Нам надо достичь минимальной разницы между самым большим и самым маленьким элементами.
    Минимальная разница будет всегда 0, так как мы подгоним один из элементов под другой.
    Таким образом у нас всего 3 варианта: взять и заменять первый и последний, первые два или последние два.
    """

    def minimize_sum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-3] - nums[0], nums[-2] - nums[1])
