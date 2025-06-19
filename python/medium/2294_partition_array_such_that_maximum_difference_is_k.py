class Solution:
    """
    Grade[Medium]
    Topics[Array, Greedy, Sorting]

    You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such
    that each element in nums appears in exactly one of the subsequences.

    Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in
    each subsequence is at most k.

    A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without
    changing the order of the remaining elements.

    Constraints:
        n == nums.length
        2 <= n <= 1000
        1 <= nums[i] <= 10^9
    """

    def partitionArray(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n) + O(n log n) - Beats 41.24%
        Space Complexity: O(n) - только для частного случая с нулями, иначе O(1) - Beats 5.15%

        Логика двух pointer'ов. Проходим по отсортированному списку двумя указателям.
        Первый указывает на начало подсписка, второй ищет его конец.
        После идёт смещение первого указателя ко второму.
        """
        if k == 0:
            return len(set(nums))

        length = len(nums)
        nums.sort()
        counter = 0
        i, j = 0, 0
        while i <= length - 1:
            j += 1
            while j <= length - 1 and nums[j] - nums[i] <= k:
                j += 1

            counter += 1
            i = j
        return counter

    def partitionArray(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n log n) - Beats 92.99%
        Space Complexity: O(1) - Beats 73.61%

        Аналогичная логика предыдущему решению, только сильно упрощенная.
        Нет необходимости сохранять индексы, мы просто запоминаем сами числа.
        Нам достаточно знать первое число в начале подсписка и сравнивать с другими в основном списке.
        """
        nums.sort()
        counter = 1
        first_num_in_subsequence = nums[0]
        for num in nums:
            if num - first_num_in_subsequence > k:
                counter += 1
                first_num_in_subsequence = num
        return counter


s = Solution()
nums = [1, 2, 3, 5, 6]
k = 2

nums = [1, 2, 3]
k = 1

nums = [2, 2, 4, 5]
k = 0
result = s.partitionArray(nums, k)
print(result)