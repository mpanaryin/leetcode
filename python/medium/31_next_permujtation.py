from math import inf
from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers]

    Do not return anything, modify nums in-place instead.

    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are all the permutations of arr:
        [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    More formally, if all the permutations of the array are sorted in one container according
    to their lexicographical order, then the next permutation of that array is the permutation
    that follows it in the sorted container. If such arrangement is not possible,
    the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1]
    does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.
    """

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        nums[i:] = reversed(nums[i:])

    def nextPermutation(self, nums: List[int]) -> None:
        max_index = len(nums)
        min_element_dict = {}
        for i in reversed(range(max_index)):  # Идём с конца, так как надо найти следующее наименьшее число
            min_element_dict[
                nums[i]] = i  # Заполняем словарь значениями и их инкдексами, чтобы понимать какие числа были
            if i != 0:
                if nums[i] > nums[i - 1]:  # Нашли число, где нужна перестановка
                    for need_item in sorted(
                        list(min_element_dict.keys())
                    ):  # Поиск числа, которое подойдёт для перестановки
                        if need_item > nums[i - 1]:
                            nums[min_element_dict[need_item]] = nums[i - 1]
                            nums[i - 1] = need_item
                            break
                    else:  # Если число не найдено, меняем текущее соприкасающееся
                        temp = nums[i]
                        nums[i] = nums[i - 1]
                        nums[i - 1] = temp

                    sort_nums = sorted(
                        nums[i:]
                    )  # Осталось отсортировать все числа, которые мы проходили до перестановки
                    temp_ind = 0
                    for j in range(i, max_index):
                        nums[j] = sort_nums[temp_ind]
                        temp_ind += 1
                    return
        nums.sort()  # Если нечего перестанавливать, просто сортируем начальный массив




lst = [5, 4, 7, 5, 3, 2]
s = Solution()
result = s.nextPermutation(lst)
print('result: ', lst)
