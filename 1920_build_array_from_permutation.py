class Solution:
    """
    Grade[Easy]

    Given a zero-based permutation nums (0-indexed), build an array ans of the same length
    where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

    A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

    Constraints:
        1 <= nums.length <= 1000
        0 <= nums[i] < nums.length
        The elements in nums are distinct.

    Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?
    """

    def buildArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(N) - Beats 44.72%
        Space complexity: O(N) - Beats 13.03%
        """
        return [nums[nums[i]] for i in range(len(nums))]

    def buildArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(N) - Beats 5.86%
        Space complexity: O(1) - Beats 84.60%
        """
        n = len(nums)
        # Build the final value on the first iteration
        for i in range(n):
            nums[i] += 1000 * (nums[nums[i]] % 1000)
        # Modified to final value on the second iteration
        for i in range(n):
            nums[i] //= 1000
        return nums


nums = [0, 2, 1, 5, 3, 4]
nums = [5, 0, 1, 2, 3, 4]
s = Solution()
result = s.buildArray(nums)
print(result)
