from typing import List


class Solution:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i.
    In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n
    Return the minimum number of jumps to reach nums[n - 1].
    The test cases are generated such that you can reach nums[n - 1].
    """
    def jump(self, nums: List[int]) -> int:
        # Initialize reach (maximum reachable index), count (number of jumps), and last (rightmost index reached)
        reach, count, last = 0, 0, 0

        # Loop through the array excluding the last element
        for i in range(len(nums) - 1):
            # Update reach to the maximum between reach and i + nums[i]
            reach = max(reach, i + nums[i])
            print('reach: ', reach)

            # If i has reached the last index that can be reached with the current number of jumps
            if i == last:
                print(last)
                # Update last to the new maximum reachable index
                last = reach
                # Increment the number of jumps made so far
                count += 1

        # Return the minimum number of jumps required
        return count

s = Solution()
result = s.jump([2,3,3,1,4,1])
print(result)
