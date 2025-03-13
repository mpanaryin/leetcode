class Solution:
    """
    Given an integer array nums sorted in non-decreasing order,
    return an array of the squares of each number sorted in non-decreasing order.

    Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.
    """
    def sorted_squares(self, nums: list[int]) -> list[int]:
        """most easy"""
        return sorted([num**2 for num in nums])

    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        2 pointers
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(nums)
        ans = [0] * n
        start, end = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[start]) >= abs(nums[end]):
                ans[i] = nums[start] * nums[start]
                start += 1
            else:
                ans[i] = nums[end] * nums[end]
                end -= 1
        return ans


nums = [-4, -1, 0, 3, 10]
s = Solution()
result = s.sortedSquares(nums)
print('result', result)
