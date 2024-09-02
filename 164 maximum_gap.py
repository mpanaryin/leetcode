from collections import defaultdict


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the maximum difference between two successive elements in
        its sorted form. If the array contains less than two elements, return 0.

        You must write an algorithm that runs in linear time and uses linear extra space.

        Будем решать через сортировку ведер
        """
        low = min(nums)
        high = max(nums)
        length = len(nums)
        if length <= 2 or high == low:
            return high - low
        # Заполняем корзины. Алгоритм можно только запомнить
        # Самое больше число кладём в последнюю, а остальные распределяем по формуле:
        # (num-low)*(length-1)//(high-low)
        buckets = defaultdict(list)
        for num in nums:
            if num == high:
                buckets[length-2].append(num)
            else:
                buckets[(num-low)*(length-1)//(high-low)].append(num)
        # Дальше зная суть алгоритма, нам нужно знать минимальное и
        # максимальное значения ближайших корзин для дальнейшего сравнения
        candidates = [[min(buckets[i]), max(buckets[i])] for i in range(length-1) if buckets[i]]
        # После вычисляем наибольшее значение, т.е. наш gap
        return max(y[0]-x[1] for x, y in zip(candidates, candidates[1:]))


nums1 = [3, 6, 9, 1]
nums2 = [3, 14, 15, 83, 6, 4, 19, 20, 40]
s = Solution()
result = s.maximumGap(nums2)
print(result)