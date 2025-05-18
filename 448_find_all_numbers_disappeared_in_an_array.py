class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table]

    Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not appear in nums.

    Constraints:
    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i] <= n

    Note: Could you do it without extra space and in O(n) runtime?
    You may assume the returned list does not count as extra space.
    """

    def find_disappeared_numbers1(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n) - мы проходим один раз nums и 1 раз при создании set
        Space complexity: O(n) - мы всё же создаём новый set и для nums и для всех чисел
        """
        return list({n for n in range(1, len(nums) + 1)}.difference(nums))

    def find_disappeared_numbers2(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n) - мы проходим один раз nums и 1 раз при создании set
        Space complexity: O(n) - мы всё же создаём новый set num_range
        """
        num_range = {n for n in range(1, len(nums) + 1)}
        for num in nums:
            if num in num_range:
                num_range.remove(num)
        return list(num_range)

    def find_disappeared_numbers3(self, nums: list[int]) -> list[int]:
        """
        Самое умное решение:
        1) Индекс массива используется как способ «отметить» присутствие числа в массиве.
        2) Если число k встречается в массиве, то элемент массива по индексу k - 1 отмечается
        (например, меняется знак).
        3) В конце проходим по массиву, и те позиции, которые остались неотмеченными (положительными),
        говорят нам о том, что числа (индекс + 1) не встретились в массиве.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        ans = []
        for c in nums:
            nums[abs(c)-1] = -abs(nums[abs(c)-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
