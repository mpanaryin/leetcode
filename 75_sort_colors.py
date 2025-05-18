from typing import List


class Solution:
    """
    Grade [Medium]
    Topics[Array, Two Pointers, Sorting]

    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the
    same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

    Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

    Follow up: Could you come up with a one-pass algorithm using only constant extra space?
    """

    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n log n)
        Space complexity: O(1)
        """

        def help_func(nums, start, end):
            # Берем средний элемент из уже отрубленного
            # массива или средний из начального
            q = nums[(start + end) // 2]
            # Эти и дальнейшие +/- 1 защищают нас от
            # бесконечного цикла при дубликатах
            i = start - 1
            j = end + 1
            while True:
                i += 1
                # Просто идём по числам и если слева есть число больше
                # чем то среднее, что мы выбрали, то тормозим
                # и в дальнейшем его поменяем с числом справа
                while nums[i] < q:
                    i += 1
                # Аналогичная ситуация, только ищем числа меньше, чем те,
                # что выбранный нами элемент.
                j -= 1
                while nums[j] > q:
                    j -= 1

                # Если дошли до того, что у нас совпали индексы идя слева и справа,
                # то дробим массив уходим в рекурсию. На данном проходе отсортировали
                # всё что могли
                if i >= j:
                    return j

                nums[i], nums[j] = nums[j], nums[i]

        def quick_sort(nums, start, end):
            if start < end:
                p = help_func(nums, start, end)
                quick_sort(nums, start, p)
                quick_sort(nums, p + 1, end)

        quick_sort(nums, 0, len(nums) - 1)

    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[min_index], nums[i] = nums[i], nums[min_index]

    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        red = 0
        white = 0
        blue = len(nums) - 1
        # Проходим по всем элементам пока центр не будет рядом с концом
        while white <= blue:
            # Если средний равен 0, то меняем местами с левым
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            # Если средний равен 1, то он на месте, увеличиваем индекс
            elif nums[white] == 1:
                white += 1
            # В противном случае средний равен 2, и меняем его с правым
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


nums = [2, 0, 2, 1, 1, 0]
s = Solution()
s.sortColors(nums)
print(nums)
