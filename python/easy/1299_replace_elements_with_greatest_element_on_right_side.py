class Solution:
    """
    Grade[Easy]
    Topics[Array]

    Given an array arr, replace every element in that array with the greatest element
    among the elements to its right, and replace the last element with -1.

    After doing so, return the array.

    Constraints:
    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
    """

    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = maximum
            maximum = max(maximum, current)
        arr[-1] = -1
        return arr


arr = [17, 18, 5, 4, 6, 1]
s = Solution()
result = s.replaceElements(arr)
print(result)
print(arr)
