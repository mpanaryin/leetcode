from functools import cmp_to_key


class Solution:
    """
    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

    Since the result may be very large, so you need to return a string instead of an integer.
    """
    def largestNumber(self, nums: list[int]) -> str:
        def cmp_func(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        str_nums = [str(num) for num in nums]
        str_nums.sort(key=cmp_to_key(cmp_func))
        return ''.join(reversed(str_nums)).lstrip('0') or '0'


nums1 = [10, 2]
nums2 = [9, 3, 34, 30, 5, 55]
nums3 = [432, 43243]
nums4 = [111311, 1113]
nums5 = [311, 3]
nums6 = [344, 3]
s = Solution()
result = s.largestNumber(nums5)
print(result)
