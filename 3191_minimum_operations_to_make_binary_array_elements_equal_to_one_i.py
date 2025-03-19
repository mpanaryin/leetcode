from collections import deque


class Solution:
    """
    Grade [Medium]

    You are given a binary array nums.

    You can do the following operation on the array any number of times (possibly zero):

    Choose any 3 consecutive elements from the array and flip all of them.
    Flipping an element means changing its value from 0 to 1, and from 1 to 0.

    Return the minimum number of operations required to make all elements in nums equal to 1.
    If it is impossible, return -1.

    Constraints:
    3 <= nums.length <= 10^5
    0 <= nums[i] <= 1
    """

    def minOperations1(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        flip_queue = deque()  # Сохраняем индексы переворотов
        count = 0  # Итоговое количество переворотов

        for i in range(len(nums)):
            # Удаляем перевороты, которые старше чем 3 последние индекса (на них уже не повлиять)
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()
            # Если текущему элементу нужен переворот
            if (nums[i] + len(flip_queue)) % 2 == 0:
                # Мы не можем перевернуть триплет в конце списка
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flip_queue.append(i)

        return count

    def minOperations2(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(2, len(nums)):
            # Проходим триплеты и смотрим только на последний элемент
            if nums[i - 2] == 0:
                count += 1
                # Переворачиваем триплет
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == len(nums):
            return count
        return -1

    def minOperations3(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1

        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1
        return count


nums = [0, 1, 1, 1, 0, 0]
s = Solution()
result = s.minOperations(nums)
print(result)
print(nums)