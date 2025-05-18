class Solution:
    """
    Grade[Medium]
    Topics[Array, Binary Search, Prefix Sum]

    You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

    Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.
    A Zero Array is an array with all its elements equal to 0.

    Return the minimum possible non-negative value of k, such that after processing the first k queries
    in sequence, nums becomes a Zero Array. If no such k exists, return -1.

    Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 5 * 10^5
    1 <= queries.length <= 10^5
    queries[i].length == 3
    0 <= l(i) <= r(i) < nums.length
    1 <= val(i) <= 5
    """
    def min_zero_array(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Мой вариант, ловим TLE
        Time Complexity: O(N*M)
        """
        k = 0
        total_sum = sum(nums)
        if total_sum == 0:
            return k
        for q in queries:
            k += 1
            for i in range(q[0], q[1] + 1):
                if nums[i] == 0:
                    continue
                diff_value = min(nums[i], q[2])
                total_sum -= diff_value
                nums[i] -= diff_value
                if total_sum == 0:
                    return k
        return -1

    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Time Complexity: O(N+M)
        Space Complexity: O(N)
        """
        n = len(nums)
        total_sum = 0
        k = 0
        diff = [0] * (n + 1)  # Разностной массив
        # Проходим по длине массива
        for index in range(n):
            # Проходим через запросы пока текущее число не будет равно 0
            while total_sum + diff[index] < nums[index]:
                k += 1
                # Если мы не смогли уменьшить число до 0 за проход по всем queries
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]
                # 1. Если i < left запрос затрагивает более позднюю часть nums,
                # поэтому мы сохраняем его для последующей обработки.
                # 2. Если left ≤ i ≤ right, то запрос немедленно релевантен и должен быть применен.
                # 3. Если right < i, то запрос больше не нужен для текущего индекса и его можно игнорировать.
                if right >= index:
                    diff[max(left, index)] += val
                    diff[right + 1] -= val
            # Увеличить total_sum на значение diff[index]
            total_sum += diff[index]
        return k


nums = [10]
queries = [[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]]
s = Solution()
result = s.minZeroArray(nums, queries)
print(result)
