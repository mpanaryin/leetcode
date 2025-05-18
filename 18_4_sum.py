from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers, Sorting]

    Given an array nums of n integers, return an array of all
    the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n³)
        Space complexity: O(n)
        """

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1

            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()
        return kSum(nums, target, 4)


class BadSolution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        if sum(nums[-4:]) < target:
            return []
        end_third_for = False
        end_second_for = False
        for ind1, val1 in enumerate(nums[0:-3]):
            for ind2, val2 in enumerate(nums[ind1 + 1:-2]):
                if end_second_for:
                    break
                for ind3, val3 in enumerate(nums[ind2 + ind1 + 2:-1]):
                    if end_third_for:
                        break
                    for ind4, val4 in enumerate(nums[ind2 + ind3 + ind1 + 3:]):
                        val_list = [val1, val2, val3, val4]
                        val_list.sort()
                        res = sum(val_list)
                        if not ind2 and not ind1 and res > target:
                            end_third_for = True

                        if not ind2 and not ind3 and not ind4 and res > target:
                            print(ind1, ind2, ind3)
                            return list(result)
                        if res > target:
                            break
                        if res == target:
                            result.add(tuple(val_list))
        return list(result)
