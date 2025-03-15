class Solution:
    """
    Grade[Easy]

    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4
    """
    def validMountainArray(self, arr: list[int]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if len(arr) < 3:
            return False
        up = None
        down = None
        for i in range(len(arr) - 1):
            # Условие при котором мы идём наверх, если оно нарушается, то сразу false
            if arr[i] < arr[i + 1]:
                if up is None or up is True:
                    up = True
                else:
                    return False
            # Условие при котором мы идём вниз, если оно нарушается, то сразу false
            elif arr[i] > arr[i + 1]:
                if (up and down is None) or down is True:
                    up = False
                    down = True
                else:
                    return False
            # Повтор чисел, сразу false
            else:
                return False
        # True только в случае, если мы не в состоянии подъёма, но в состоянии спуска
        return True and not up and down

    def validMountainArray2(self, arr: list[int]) -> bool:
        """
        Решение с сайта
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if len(arr) < 3:
            return False
        l = 0
        r = len(arr) - 1
        while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]:
            l += 1
        while r - 1 > 0 and arr[r] < arr[r - 1]:
            r -= 1
        return l == r


nums1 = [0, 3, 2, 1]
nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = Solution()
result = s.validMountainArray(nums3)
print(result)
print(nums3)
