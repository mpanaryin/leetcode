class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers]

    Given an integer array nums, move all 0's to the end of it while maintaining the relative order
    of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    """

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        index = None
        for i in range(len(nums)):
            # Если у нас уже есть 0, то меняем местами с не нулём, чтобы 0 оказался справа
            if index is not None and nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                # Догоняем i и попутно ищем нули, останавливаемся на первом попавшемся нуле
                while index <= i:
                    index += 1
                    if nums[index] == 0:
                        break
            # Ищем первый 0
            elif index is None and nums[i] == 0:
                index = i


nums = [0, 1, 0, 3, 12]
s = Solution()
result = s.moveZeroes(nums)
print(result)
print(nums)
