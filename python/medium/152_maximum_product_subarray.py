class Solution:
    """
    Grade[Medium]
    Topics[Array, Dynamic Programming]

    Given an integer array nums, find a subarray
    that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    Constraints:
    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit
    in a 32-bit integer.
    """

    def maxProduct(self, nums: list[int]) -> int:
        """
        Вычислить префиксное произведение в nums.
        Вычислить суффиксное произведение в nums (reversed_nums).
        Возврат максимального значения.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        reversed_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reversed_nums[i] *= reversed_nums[i - 1] or 1
        return max(nums + reversed_nums)

    def maxProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            if n == 0:
                cur_max = cur_min = 1
                continue

            temp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(temp, n * cur_min, n)
            res = max(res, cur_max)

        return res


nums1 = [2, 3, -2, 4, 3, 0]
nums2 = [-2, 0, -1]
s = Solution()
result = s.maxProduct(nums1)
print(result)
