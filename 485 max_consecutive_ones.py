class Solution:
    """
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
    """
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum = counter = 0
        for num in nums:
            if num:
                counter += 1
                if counter > maximum:
                    maximum = counter
            else:
                counter = 0
        return maximum


nums = [1, 1, 0, 1, 1, 1]
s = Solution()
result = s.findMaxConsecutiveOnes(nums)
print('result', result)
