class Solution:
    """
    Grade[Easy]

    Given an integer array nums, return the number of subarrays of length 3 such that the sum of
    the first and third numbers equals exactly half of the second number.

    Constraints:
        3 <= nums.length <= 100
        -100 <= nums[i] <= 100
    """

    def countSubarrays(self, nums: list[int]) -> int:
        """
        Time complexity: O(N) - Beats 91.43%
        Space complexity: O(1) - Beats 7.35%
        """
        counter = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i+2] == nums[i+1] / 2:
                counter += 1
        return counter


nums = [1, 2, 1, 4, 1]
s = Solution()
result = s.countSubarrays(nums)
print(result)
