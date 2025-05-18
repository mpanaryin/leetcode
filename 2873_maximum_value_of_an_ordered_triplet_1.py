class Solution:
    """
    Grade[Easy]
    Topics[Array]

    You are given a 0-indexed integer array nums.

    Return the maximum value over all triplets of indices (i, j, k) such that i < j < k.
    If all such triplets have a negative value, return 0.

    The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

    Constraints:
    3 <= nums.length <= 100
    1 <= nums[i] <= 10^6
    """

    def maximumTripletValue(self, nums: list[int]) -> int:
        """
        Time complexity: O(n^3)
        Space complexity: O(1)
        """
        result = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                result = max((nums[i] - nums[j]) * max(nums[j + 1:]), result)
        return result

    def maximumTripletValue(self, nums: list[int]) -> int:
        """
        Greedy
        Time complexity: O(n^2)
        Space complexity: O(1)

        When j and k of the triplet (i,j,k) are fixed, it can be known from the value formula
        (nums[i]−nums[j])×nums[k] that (nums[i]−nums[j])×nums[k] is maximized when nums[i] takes the maximum value
        in the interval [0,j). Use two nested loops to enumerate k and j respectively, while using m to maintain
        the maximum value of [0,j). Return the maximum value of all (m−nums[j])×nums[k] (if all values are negative,
        return 0).
        """
        n = len(nums)
        res = 0
        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return res

    def maximumTripletValue(self, nums: list[int]) -> int:
        """
        Greedy + Prefix Suffix Array
        Time complexity: O(n)
        Space complexity: O(1)

        Let the length of the array nums be n. According to the value formula (nums[i]−nums[j])×nums[k],
        it can be known that when j is fixed, the maximum value of the triplet is achieved when nums[i] and
        nums[k] respectively take the maximum values from [0,j) and [j+1,n). We use leftMax[j] and rightMax[j]
        to maintain the maximum value of the prefix [0,j) and the maximum value of the suffix [j+1,n), respectively.
        We then enumerate j in order, calculate the value (leftMax[j]−nums[j])×rightMax[j],
        and return the maximum value (if all values are negative, return 0).
        """
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res

    def maximumTripletValue(self, nums: list[int]) -> int:
        """
        Greedy
        Time complexity: O(n)
        Space complexity: O(1)

        Similar to approach 3, if we fix k, then the value of the triplet is maximized when nums[i]−nums[j]
        takes the maximum value. We can use imax to maintain the maximum value of nums[i] and dmax to maintain the
        maximum value of nums[i]−nums[j]. During the enumeration of k, update dmax and imax.
        """
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res


nums = [12, 6, 1, 2, 7]
s = Solution()
result = s.maximumTripletValue(nums)
print(result)
