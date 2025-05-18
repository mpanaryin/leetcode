from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Binary Search]

    You are given a sorted array consisting of only integers where every element appears exactly twice,
    except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

    Логика решения: мы отрезаем 1 элемент, чтобы число элементов стало чётным,
    при этом мы не вышли за пределы.
    Если центральный элемент и следующий за ним пара, значит слева нет нужного нам элемента.
    Так как все элементы идут парами.
    Следовательно начальным элементом становится центральный + 2,
    т.е. следующая предполагаемая пара.
    Это +2 достигается довольно странным способом (он неявный). Так как формула: индексы mid + 1 + end (новый центр)
    Если же пару изначально не находим, то отсекаем правую часть через: mid - 1 + end (новый центр)
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        start = 0
        end = len(nums) - 2
        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == nums[mid ^ 1]:  # если центральный элемент и следующий за ним пара
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]
