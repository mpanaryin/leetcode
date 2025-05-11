class Solution:
    """
    Grade[Easy]

    Given an integer array arr, return true if there are three consecutive odd numbers in the array.
    Otherwise, return false.

    Constraints:
        1 <= arr.length <= 1000
        1 <= arr[i] <= 1000
    """

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        Time Complexity: O(N) - Beats 100%
        Space Complexity: O(1) - Beats 88.31%
        """
        if len(arr) < 3:
            return False

        counter = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                counter = 0
            else:
                counter += 1
                if counter == 3:
                    return True
        return False


arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
s = Solution()
result = s.threeConsecutiveOdds(arr)
print(result)
