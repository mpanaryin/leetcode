from typing import List


class Solution:
    """
    Grade [Easy]

    Given an integer array nums, move all the even integers at the beginning
    of the array followed by all the odd integers.

    Return any array that satisfies this condition.

    Constraints:
    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
    """
    def sortArrayByParity1(self, nums: list[int]) -> list[int]:
        """
        Моё старое решение, судя по срезам через del, будет постоянный пересчёт индексов - плохо по времени
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

    def sortArrayByParity2(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        Моё новое решение, аналогично решению 283 со сдвигом нулей
        """
        odd_index = None
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and odd_index is not None:
                nums[i], nums[odd_index] = nums[odd_index], nums[i]
                while odd_index < i:
                    odd_index += 1
                    if nums[odd_index] % 2 != 0:
                        break
            elif odd_index is None and nums[i] % 2 != 0:
                odd_index = i

    def sortArrayByParity3(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        Решение с сайта, подходит такой обмен только из-за условия, которому не важен порядок элементов
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            # Если число чётное, то оставляем его
            if nums[start] % 2 == 0:
                start += 1
            # Если число нечетное, то меняем местами с последним элементом
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        return nums

nums = [3,1,2,4]
s = Solution2()
s.sortArrayByParity(nums)
print(nums)