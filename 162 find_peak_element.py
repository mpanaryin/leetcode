class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        A peak element is an element that is strictly greater than its neighbors.

        Given a 0-indexed integer array nums, find a peak element, and return its index.
        If the array contains multiple peaks, return the index to any of the peaks.

        You may imagine that nums[-1] = nums[n] = -∞.
        In other words, an element is always considered to be strictly greater than a
        neighbor that is outside the array.

        You must write an algorithm that runs in O(log n) time.
        """
        prev = nums[0]
        max_num = nums[0]
        max_index = 0
        for i in range(1, len(nums) - 1):
            if prev < nums[i] > nums[i + 1]:
                return i
            prev = nums[i]
            if max_num < nums[i]:
                max_num = nums[i]
                max_index = i
        return max_index if max_num >= nums[-1] else len(nums) - 1

    def btree_solution(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        # handle condition 3
        while left < right - 1:
            mid = (left + right) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right


nums1 = [1, 2, 1, 3, 5, 6, 4]
nums2 = [1, 2]
s = Solution()
result = s.findPeakElement(nums2)
print(result)