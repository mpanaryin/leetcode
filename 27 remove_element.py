from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Consider the number of elements in nums which are not equal to val be k, to get accepted,
        you need to do the following things:

        Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
        The remaining elements of nums are not important as well as the size of nums.
        Return k.

        IMPORTANT: тут важно смотреть за передаваемым nums, изменяем только его, так как это глобальная вещь
        """
        # Minimal code
        while val in nums:
            nums.remove(val)
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        """First try"""
        deletion_indexes = []
        for i, num in enumerate(nums):
            if num == val:
                deletion_indexes.append(i)
        for i, to_del in enumerate(deletion_indexes):
            nums.pop(to_del-i)
        return len(nums)

    def removeElement3(self, nums: List[int], val: int) -> int:
        """FASTEST"""
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


s = Solution()
result = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)
