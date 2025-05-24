class Solution:
    """
    Grade[Easy]
    Topics[Array, Two Pointers]

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
    element appears only once. The relative order of the elements should be kept the same.
    Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order
    they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

    Constraints:
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        unique_count = 1
        index = 0
        for i in range(len(nums)):
            if nums[i] != nums[index]:
                unique_count += 1
                index += 1
                nums[index] = nums[i]
        return unique_count


nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
result = s.removeDuplicates(nums2)
print(nums2)
