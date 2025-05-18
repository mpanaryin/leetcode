from typing import List
from collections import Counter


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers, Sorting]

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    """

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n²)
        Space complexity: O(n)
        """
        result = set()
        nums.sort()
        counter = Counter(nums)
        # Проходим по всем возможным цифрам
        for num, count in counter.items():
            skips = set()
            # Если такая цифра встречается минимум 2 раза, то мы можем попытаться найти ей отрицательную пару
            if count >= 2:
                desired_num = (num + num) * -1
                if counter.get(desired_num):
                    result.add(tuple(sorted((num, num, desired_num))))
            # Но также эта цифра может где-то пригодится и одиночной
            for num2 in counter.keys():
                # Сразу пропускаем, если встречается пара
                if num == num2 or num2 in skips:
                    continue
                desired_num = (num2 + num) * -1
                count_desired_num = counter.get(desired_num)
                # Если нужное нам число есть в нашем списке и оно не равно ни одному из тех, что мы перебираем
                if count_desired_num and (desired_num != num2 and desired_num != num):
                    result.add(tuple(sorted((num, num2, desired_num))))
            skips.add(num)
        zero_count = counter.get(0)
        if zero_count and zero_count < 3:
            result.difference_update({(0, 0, 0)})
        return list(map(lambda x: list(x), list(result)))


class Solution2:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
