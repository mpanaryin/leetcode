class Solution:
    """
    Grade[Easy]
    Topics[Array, Math, Sorting]

    You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

    A triangle is called equilateral if it has all sides of equal length.
    A triangle is called isosceles if it has exactly two sides of equal length.
    A triangle is called scalene if all its sides are of different lengths.
    Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

    Constraints:
        nums.length == 3
        1 <= nums[i] <= 100
    """

    def triangleType(self, nums: list[int]) -> str:
        """
        Time Complexity: O(1) - Beats 100%
        Space Complexity: O(1) - Beats 10.54%
        """
        if nums[0] == nums[1] == nums[2]:
            return 'equilateral'
        elif nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            if nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
                return 'isosceles'
            else:
                return 'scalene'
        return 'none'
   