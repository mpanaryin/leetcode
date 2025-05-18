class Solution:
    """
    Grade[Medium]
    Topics[Array, Math, Two Pointers]

    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    """

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time complexity: O(n)
        Space complexity: O(k)
        """
        nums_length = len(nums)
        if k // nums_length > 0:
            k = k % nums_length

        to_add = nums[nums_length - k:nums_length]
        nums[k:nums_length] = nums[0:nums_length - k]
        nums[0:k] = to_add

    def rotate(self, nums: list[int], k: int) -> None:
        """
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # normalize k

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
s.rotate(nums, k)
print(nums)
