class Solution:
    """
    Grade [Easy]

    A school is trying to take an annual photo of all the students.
    The students are asked to stand in a single file line in non-decreasing order by height.
    Let this ordering be represented by the integer array expected where expected[i] is the expected height
    of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in.
    Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].

    Constraints:
    1 <= heights.length <= 100
    1 <= heights[i] <= 100

    For info: https://leetcode.com/problems/height-checker/solutions/5286352/height-checker/
    Тут есть информация обо всех видах сортировок
    """
    def heightChecker(self, heights: list[int]) -> int:
        """
        Самое простое решение
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        result = 0
        heights_sorted = sorted(heights)
        for i in range(len(heights)):
            if heights_sorted[i] != heights[i]:
                result += 1
        return result


nums = [1, 1, 4, 2, 1, 3]
s = Solution()
result = s.heightChecker(nums)
print(result)
print(nums)
