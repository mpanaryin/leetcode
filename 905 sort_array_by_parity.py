from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, move all the even integers at the beginning
        of the array followed by all the odd integers.

        Return any array that satisfies this condition.
        """
        dif_index = 0
        nums_len = len(nums)
        for i in range(nums_len):
            current_index = i - dif_index
            if nums[current_index] % 2 != 0:
                nums.append(nums[current_index])
                del nums[current_index]
                dif_index += 1
        return nums


class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, move all the even integers at the beginning
        of the array followed by all the odd integers.

        Return any array that satisfies this condition.
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] % 2 == 0:
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        return nums

nums = [3,1,2,4]
s = Solution2()
s.sortArrayByParity(nums)
print(nums)