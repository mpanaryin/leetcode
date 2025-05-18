from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers, Binary Search, Bit Manipulation]

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

    1.Start by initializing two pointers, slow and fast, both initially pointing to the first element of the array.

    2.Move slow one step at a time, and fast two steps at a time within a loop until they meet.
    This is guaranteed to happen because there's a repeated number in the array.

    3.Once they meet, reset one of the pointers (e.g., slow) back to the first element of the array and keep
    the other pointer (e.g., fast) where it is.

    4.Now, move both pointers one step at a time within the loop until they meet again.
    The point at which they meet is the start of the cycle, which corresponds to the repeated number in the array.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        # Initialize the pointers
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the intersection point of the two pointers
        while True:
            slow = nums[slow]  # Move one step
            fast = nums[nums[fast]]  # Move two steps

            if slow == fast:
                break

        # Phase 2: Find the start of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # The start of the cycle is the repeated number
        return slow


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
