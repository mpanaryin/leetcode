class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers, Simulation]

    You are given a 0-indexed integer array nums and an integer pivot.
    Rearrange nums such that the following conditions are satisfied:

    Every element less than pivot appears before every element greater than pivot.
    Every element equal to pivot appears in between the elements less than and greater than pivot.
    The relative order of the elements less than pivot and the elements greater than pivot is maintained.
    More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position
    of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
    Return nums after the rearrangement.

    Constraints:

    1 <= nums.length <= 10^5
    -10^6 <= nums[i] <= 10^6
    pivot equals to an element of nums.
    """

    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        middle = []
        right_side = []
        left_side = []
        for i, num in enumerate(nums):
            if num > pivot:
                right_side.append(num)
            elif num < pivot:
                left_side.append(num)
            else:
                middle.append(num)
        return left_side + middle + right_side

    def pivotArray2(self, nums: list[int], pivot: int) -> list[int]:
        """
        Time Complexity: O(N)

        We perform a simultaneous forward and backwards iteration of nums,
        taking a total of O(N) time.

        Space Complexity: O(N) or O(1)

        P.S. на тестах хуже первого варианта
        """
        ans = [0] * len(nums)
        left_index = 0
        right_index = len(nums) - 1
        # forward and backwards iteration
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[left_index] = nums[i]
                left_index += 1
            if nums[j] > pivot:
                ans[right_index] = nums[j]
                right_index -= 1
        # add pivot
        while left_index <= right_index:
            ans[left_index] = pivot
            left_index += 1
        return ans


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
s = Solution()
result = s.pivotArray2(nums, pivot)
print(result)
