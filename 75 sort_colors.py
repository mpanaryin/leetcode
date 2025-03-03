from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the
        same color are adjacent, with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

        You must solve this problem without using the library's sort function.

        Do not return anything, modify nums in-place instead.
        """
        def help_func(nums, start, end):
            # Берем средний элемент из уже отрубленного
            # массива или средний из начального
            q = nums[(start+end) // 2]
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





nums = [2,0,2,1,1,0]
s = Solution()
s.sortColors(nums)
print(nums)


