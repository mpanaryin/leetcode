from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears twice except for one.
        Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.

        Xor любых двух чисел дает разницу бита как 1 и того же бита как 0.
        Таким образом, используя это, мы получаем 1 ^ 1 == 0, потому что одинаковые числа имеют одинаковые биты.
        Таким образом, мы всегда будем получать один элемент, потому что все одинаковые будут оцениваться как 0 и 0^single_number = single_number.
        Время: O(n)
        Пространство: O(1)
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor



nums = [4, 1, 2, 1, 2]
s = Solution()
s.singleNumber(nums)
