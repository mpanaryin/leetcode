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

        IMPORTANT: Мы не удаляем элементы, нам вообще всё равно на них порядок, главное что будет в начале.
        Пример: nums = [1], val = 1. По итогу мы возвращаем k = 0, а список так и остаётся [1], он не становится пустым
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
        k = 0
        for i in range(len(nums)):
            # Если текущее число в массиве не равно нашему числу
            if nums[i] != val:
                # Делаем перестановку. Если до этого не было val, то замены вообще не будет, но если было,
                # то k будет опаздывать и находится как раз на позиции val, на неё встанет наша замена.
                nums[k] = nums[i]
                k += 1
        return k


s = Solution()
result = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)
