from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Two Pointers, Sorting]

    Given an integer array nums of length n and an integer target,
    find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        return result


class Solution2:
    """
    Это лучшее решение этой задачи. Работает не только для 3х, а для любых k
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        """k отвечает за количество суммируемых элементов"""
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # Если сумма трёх наименьших чисел всё ещё больше цели, то возвращаем сразу
        current = sum(nums[:k])
        if current >= target:
            return current

        # Если сумма трёх наибольших чисел всё ещё меньше цели, то возвращаем сразу
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        # Проходим по всем элементам от начала до конца -k + 1 элементов
        for i, x in enumerate(nums[:-k + 1]):
            # Если предыдущее число равно текущему, то пропускаем
            if i > 0 and x == nums[i - 1]:
                continue
            # Берем числа от текущего индекса +1 до конца, при этом уменьшаем k
            # цель уменьшается на x, т.е. текущее исследуемое число.
            # Получаем текущую сумму
            current = self.KSumClosest(nums[i + 1:], k - 1, target - x) + x
            # Если модуль разницы "цель - текущее значение" меньше
            # чем модуль разницы "цель - сумма первых элементов до индекса k".
            if abs(target - current) < abs(target - closest):
                # Если текущее значение равно цели, то возвращаем цель
                if current == target:
                    return target
                # Иначе ближайшим значением становится текущее
                else:
                    closest = current
        return closest
