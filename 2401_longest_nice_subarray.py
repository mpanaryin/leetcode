class Solution:
    """
    Grade [Medium]

    You are given an array nums consisting of positive integers.

    We call a subarray of nums nice if the bitwise AND of every pair of elements
    that are in different positions in the subarray is equal to 0.

    Return the length of the longest nice subarray.

    A subarray is a contiguous part of an array.

    Note that subarrays of length 1 are always considered nice.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    """

    def longestNiceSubarray(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n^2 log n)
        Space Complexity: O(1)
        """
        # Binary search for the longest nice subarray length
        left, right = 0, len(nums)
        result = (
            1  # Minimum answer is 1 (as subarrays of length 1 are always nice)
        )

        while left <= right:
            length = left + (right - left) // 2
            if self._can_form_nice_subarray(length, nums):
                result = length  # Update the result
                left = length + 1  # Try to find a longer subarray
            else:
                right = length - 1  # Try a shorter length

        return result

    def _can_form_nice_subarray(self, length: int, nums: list[int]) -> bool:
        if length <= 1:
            return True  # Subarray of length 1 is always nice

        # Try each possible starting position for subarray of given length
        for start in range(len(nums) - length + 1):
            bit_mask = 0  # Tracks the bits used in the current subarray
            is_nice = True

            # Check if the subarray starting at 'start' with 'length' elements is nice
            for pos in range(start, start + length):
                # If current number shares any bits with existing mask,
                # the subarray is not nice
                if bit_mask & nums[pos] != 0:
                    is_nice = False
                    break
                bit_mask |= nums[pos]  # Add current number's bits to the mask

            if is_nice:
                return True  # Found a nice subarray of the specified length

        return False  # No nice subarray of the given length exists

    def longestNiceSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        used_bits = 0  # Tracks bits used in current window
        window_start = 0  # Start position of current window
        max_length = 0  # Length of longest nice subarray found

        for window_end in range(len(nums)):
            # If current number shares bits with window, shrink window from left
            # until there's no bit conflict
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[
                    window_start
                ]  # Remove leftmost element's bits
                window_start += 1  # Shrink window from left

            # Add current number to the window
            used_bits |= nums[window_end]

            # Update max length if current window is longer
            max_length = max(max_length, window_end - window_start + 1)

        return max_length


nums = [1, 3, 8, 48, 10]
# nums = [3, 1, 5, 11, 13]
s = Solution()
result = s.longestNiceSubarray(nums)
print(result)
print(nums)
