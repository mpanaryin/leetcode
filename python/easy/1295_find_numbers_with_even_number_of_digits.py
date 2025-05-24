class Solution:
    """
    Grade[Easy]
    Topics[Array, Math]

    Given an array nums of integers, return how many of them contain an even number of digits.

    Constraints:
    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5
    """
    def findNumbers(self, nums: list[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])


nums = [12, 345, 2, 6, 7896]
s = Solution()
result = s.findNumbers(nums)
print('result', result)
