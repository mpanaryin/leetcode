class Solution:
    """
    Grade[Medium]
    Topics[Array, Hash Table, Union Find]

    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    """
    @staticmethod
    def counting_sort_with_negatives(arr):
        # Находим минимальное и максимальное значения в массиве
        min_val = min(arr)
        max_val = max(arr)
        # Диапазон значений
        range_of_elements = max_val - min_val + 1
        # Создаем массив подсчетов (C) размером range_of_elements и заполняем его нулями
        count = [0] * range_of_elements
        # Подсчитываем количество каждого элемента в исходном массиве
        for num in arr:
            count[num - min_val] += 1
        # Преобразуем массив подсчетов в массив накопленных сумм
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        # Создаем выходной массив (B) такой же длины, как и исходный массив
        output = [0] * len(arr)
        # Проходим по исходному массиву с конца и размещаем элементы в выходном массиве
        for num in reversed(arr):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
        # Возвращаем отсортированный массив
        return output

    def longest_consecutive(self, nums: list[int]) -> int:
        """Memory Limit Exceeded"""
        nums = list(set(nums))
        nums_len = len(nums)
        if not nums_len:
            return 0
        sorted_nums = self.counting_sort_with_negatives(nums)
        max_result = 1
        current = 1
        for i in range(nums_len - 1):
            if sorted_nums[i] == sorted_nums[i+1] or sorted_nums[i] + 1 == sorted_nums[i+1]:
                current += 1
                if current > max_result:
                    max_result = current
            else:
                current = 1
        return max_result

    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        nums = set(nums)
        nums_len = len(nums)
        if not nums_len:
            return 0
        max_result = 1
        for num in nums:
            current_result = 1
            if (num - 1) not in nums:
                while (num + current_result) in nums:
                    current_result += 1
                max_result = current_result if current_result > max_result else max_result
        return max_result


nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums3 = []
nums4 = [0, -1]
nums5 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
s = Solution()
result = s.longestConsecutive(nums5)
print(result)
