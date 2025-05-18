class Solution:
    """
    Grade[Easy]
    Topics[Array, Enumeration]

    Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

    A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c
    Where |x| denotes the absolute value of x.

    Return the number of good triplets.

    Constraints:
        3 <= arr.length <= 100
        0 <= arr[i] <= 1000
        0 <= a, b, c <= 1000
    """

    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """
        Time Complexity: O(n^3) - Beats 38.71%
        Space Complexity: O(1) - Beats 24.73%
        """
        counter = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        counter += 1
        return counter

    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """
        Оптимизированная версия начальной, у нас не будет необходимости
        заходить в третий цикл во многих случаях.

        Time Complexity: O(n^3) - Beats 90.73%
        Space Complexity: O(1) - Beats 24.73%
        """
        counter = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            counter += 1
        return counter

    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """
        Решение с сайта

        Time Complexity: O(n^2+ nS) - Beats 95.56%
        Space Complexity: O(S) - Beats 61.96%
        """
        ans = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
            for k in range(arr[j], 1001):
                total[k] += 1

        return ans


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
s = Solution()
result = s.countGoodTriplets(arr, a, b, c)
print(result)
