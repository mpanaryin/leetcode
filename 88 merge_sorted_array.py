from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
        that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Выстраданное решение
        Time Complexity: O(m + n)
        Space Complexity: O(m)
        """
        if not m:
            nums1[:] = nums2
        if not n:
            return
        nums1_copy = nums1[:]
        _m = _n = 0
        for i in range(m+n):
            if _n == n:
                nums1[i] = nums1_copy[_m]
                _m += 1
                continue
            elif _m == m:
                nums1[i] = nums2[_n]
                _n += 1
                continue
            if nums1_copy[_m] <= nums2[_n]:
                nums1[i] = nums1_copy[_m]
                _m += 1
            else:
                nums1[i] = nums2[_n]
                _n += 1

    def merge3(self, nums1: list[int], m: int, nums2: list[int], n: int):
        """
        Идеальное решение
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # p1 указывает на последний элемент валидной части nums1
        p1 = m - 1
        # p2 указывает на последний элемент nums2
        p2 = n - 1
        # p указывает на последнюю позицию в nums1 (общая длина m+n)
        p = m + n - 1

        # Сливаем массивы с конца
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Если остались элементы в nums2, копируем их (если остались элементы в nums1, они уже на месте)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

nums1 = [0]
m = 0
nums2 = [2,5,6]
n = 3

s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)
