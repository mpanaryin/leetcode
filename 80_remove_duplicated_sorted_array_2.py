from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers]

    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that
    each unique element appears at most twice. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result
    be placed in the first part of the array nums. More formally,
    if there are k elements after removing the duplicates,
    then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array
    in-place with O(1) extra memory.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if len(nums) <= 2:
            return len(nums)

        insert_pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos

    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        current_num = None
        dif_index = 0
        result = 0
        for i in range(len(nums)):
            current_index = i - dif_index
            if nums[current_index] == '_':
                break

            if current_num != nums[current_index]:
                counter = 1
                current_num = nums[current_index]
            else:
                counter += 1

            if counter > 2:
                del nums[current_index]
                nums.append('_')
                dif_index += 1
            else:
                result += 1
        return result


nums = [1, 1, 1, 2, 2, 3]

s = Solution()
result = s.removeDuplicates(nums)
print(result)
