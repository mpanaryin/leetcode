import math
from collections import deque

from sortedcontainers import SortedSet


class Solution:
    """
    Grade [Easy]

    Given an integer array nums, return the third distinct maximum number in this array.
    If the third maximum does not exist, return the maximum number.

    Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    """

    def third_max1(self, nums: list[int]) -> int:
        """
        Плохое решение из-за сортировки, но рабочее/
        Сортировка даст нам:
        Time complexity: O(n log n)
        Space complexity: O(Q) - где Q размер queue, т.е. всего 3 элемента, так что можно считать как O(1)
        """
        nums.sort()
        queue = deque(maxlen=3)
        current_max = nums[0]
        queue.append(current_max)
        for i in range(1, len(nums)):
            if nums[i] > current_max:
                current_max = nums[i]
                queue.append(nums[i])
        return min(queue) if len(queue) == 3 else max(queue)

    def third_max2(self, nums: list[int]) -> int:
        """
        Очень плохое решение
        Time complexity: O(n)
        Space complexity: O(Q+M) - где Q размер queue, т.е. всего 3 элемента, так что можно считать как O(1) и
        M, где M - элементы seen, т.е. все уникальные элементы
        """
        queue = deque(maxlen=3)
        current_max = nums[0]
        queue.append(current_max)
        seen = {nums[0]}
        for i in range(1, len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
            if nums[i] > current_max:
                current_max = nums[i]
                queue.append(nums[i])
            else:
                if len(queue) == 1:
                    queue.appendleft(nums[i])
                elif len(queue) == 2:
                    if queue[0] > nums[i]:
                        queue.appendleft(nums[i])
                    elif queue[0] < nums[i]:
                        queue.appendleft(queue[0])
                        queue[1] = nums[i]
                else:
                    if queue[1] < nums[i] and queue[0] != nums[i]:
                        queue[1], queue[0] = nums[i], queue[1]
                    elif queue[0] < nums[i]:
                        queue[0] = nums[i]
        return min(queue) if len(queue) == 3 else max(queue)

    def third_max3(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(Q) - где Q размер queue, т.е. всего 3 элемента, так что можно считать как O(1)
        """
        # Sorted set to keep elements in sorted order.
        sorted_nums = SortedSet()
        # Iterate on all elements of 'nums' array.
        for num in nums:
            # Do not insert same element again.
            if num in sorted_nums:
                continue
            # If sorted set has 3 elements.
            if len(sorted_nums) == 3:
                # And the smallest element is smaller than current element.
                if sorted_nums[0] < num:
                    # Then remove the smallest element and push the current element.
                    sorted_nums.discard(sorted_nums[0])
                    sorted_nums.add(num)
            # Otherwise push the current element of nums array.
            else:
                sorted_nums.add(num)
        # If sorted set has three elements return the smallest among those 3.
        if len(sorted_nums) == 3:
            return sorted_nums[0]
        # Otherwise return the biggest element of nums array.
        return sorted_nums[-1]

    def thirdMax(self, nums: list[int]) -> int:
        """
        Лучшее решение, но если будет расти количество значений
        (условно первые наибольшие 10, то будут проблемы)
        Time complexity: O(n)
        Space complexity: O(1)
        """
        # Наши 3 значения
        first_max = -math.inf
        second_max = -math.inf
        third_max = -math.inf
        for num in nums:
            # Проверяем, есть ли у нас уже такое число
            if first_max == num or second_max == num or third_max == num:
                continue
            # Если текущее число больше всех, что у нас есть, то необходимо сделать сдвиг всех чисел
            if first_max <= num:
                third_max = second_max
                second_max = first_max
                first_max = num
            # Если число больше второго числа, значит оно должно стать вторым, сдвинув текущее второе
            elif second_max <= num:
                third_max = second_max
                second_max = num
            # Если число больше третьего, то просто заменяем его
            elif third_max <= num:
                third_max = num
        # Если третье число отсутствует, то возвращаем максимальное значение
        if third_max == -math.inf:
            return first_max
        # Если у нас все три значения, то возвращаем минимальное
        return third_max


nums = [2, 2, 3, 1]
nums = [5, 2, 2]
nums = [1, 2, 2, 5, 3, 5]
nums = [5, 2, 4, 1, 3, 6, 0]
s = Solution()
result = s.thirdMax(nums)
print(result)
print(nums)

