class Solution:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    """
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        if k // nums_length > 0:
            k = k % nums_length

        to_add = nums[nums_length-k:nums_length]
        nums[k:nums_length] = nums[0:nums_length-k]
        nums[0:k] = to_add


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
s.rotate(nums, k)
print(nums)
