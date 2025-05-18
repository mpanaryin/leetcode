from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Backtracking]

    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
    frequency of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is
    less than 150 combinations for the given input.

    Логика решения:
    1. Создаётся пустой двумерный массив dp длиной target
    2. Проходим по всем возможных кандидатам
    3. По каждому кандидату создаём вложенный range цикл, начало которого - это сам элемент, а конец target + 1
    4. В каждом первом проходе вложенного цикла добавляем по индексу кандидата самого кандидата
    5. Создаётся ещё один вложенный цикл, в котором проходят по элементам dp[i - c],
    т.е. это все возможные комбинации
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(2^t × k)
        Space complexity: O(t × k)
        """
        dp = [[] for _ in range(target + 1)]
        print(dp)
        for c in candidates:  # O(N): for each candidate
            for i in range(c, target + 1):  # O(M): for each possible value <= target
                if i == c:
                    dp[i].append([c])
                print(dp)
                print('dp[i - c]: ', dp[i - c])
                for comb in dp[i - c]:
                    dp[i].append(comb + [c])  # O(M) worst: for each combination
        return dp[-1]



s = Solution()
s.combinationSum([2,3,6,7], 7)
