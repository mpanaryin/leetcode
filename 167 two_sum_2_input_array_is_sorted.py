class Solution:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
    and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of
    length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.
    """
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Было на удивление легко"""
        length = len(numbers)
        start = 0
        end = length - 1
        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        return [start+1, end+1]


numbers1 = [2, 7, 11, 15]
target1 = 9

numbers2 = [2, 3, 4]
target2 = 6

numbers3 = [-1, 0]
target3 = -1

s = Solution()
result = s.twoSum(numbers2, target2)
print(result)
