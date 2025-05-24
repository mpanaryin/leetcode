class Solution:
    """
    Grade[Easy]
    Topics[Array, Binary Search, Counting]

    Given an array nums sorted in non-decreasing order, return the maximum between the number of
    positive integers and the number of negative integers.

    In other words, if the number of positive integers in nums is pos and the number of negative integers
    is neg, then return the maximum of pos and neg.
    Note that 0 is neither positive nor negative.

    Constraints:
    1 <= nums.length <= 2000
    -2000 <= nums[i] <= 2000
    nums is sorted in a non-decreasing order.
    """

    def maximum_count(self, nums: list[int]) -> int:
        """
        Первый вариант, самый простой
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        positive = negative = 0
        for num in nums:
            if num < 0:
                negative += 1
            elif num > 0:
                positive += 1
        return max(positive, negative)

    def maximumCount(self, nums: list[int]) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        negative = positive = negative_end = positive_start = None
        for i, num in enumerate(nums):
            # Определяем, встречали ли отрицательные/положительные числа
            if num < 0:
                negative = True
            elif num > 0:
                positive = True
            # Определяем конец отрицательных
            if not negative_end and negative and num >= 0:
                negative_end = i
            # Определяем начало положительных, если оно есть, цикл можно завершить
            if positive and num > 0:
                positive_start = i
                break
        return max(
            len(nums[:negative_end]) if negative else 0,
            len(nums[positive_start:]) if positive else 0
        )


nums1 = [-3, -2, -1, 0, 0, 1, 2]
nums2 = [5, 20, 66, 1314]
s = Solution()
result = s.maximumCount(nums1)
print('result', result)
