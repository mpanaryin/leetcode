class Solution:
    """
    Grade[Easy]
    Topics[Array]

    Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e.,
    nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

    Return the maximum difference. If no such i and j exists, return -1..

    Constraints:
        n == nums.length
        2 <= n <= 1000
        1 <= nums[i] <= 10^9
    """

    def maximumDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(n^2) - Beats 5.00%
        Space complexity: O(1) - Beats 59.91%
        """
        max_diff = nums[1] - nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_diff = max(max_diff, nums[j] - nums[i])
        return -1 if max_diff <= 0 else max_diff

    def maximumDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(n^2) - Beats 51.92%
        Space complexity: O(1) - Beats 89.57%
        """
        nums.reverse()
        max_diff = nums[0] - nums[1]
        max_value = nums[0]
        i = 0
        while i < len(nums) - 1:
            max_value = max(max_value, nums[i])
            for j in range(i + 1, len(nums)):
                max_diff = max(max_diff, max_value - nums[j])
                if nums[j] >= max_value:
                    i = j - 1
                    break
            else:
                # Если оказались здесь, значит все числа идут по убыванию и
                # максимальная разница у нас уже получена
                break
            i += 1
        return -1 if max_diff <= 0 else max_diff


s = Solution()
result = s.maximumDifference([7, 1, 5, 4])
print(result)