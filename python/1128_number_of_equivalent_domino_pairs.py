from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Counting]

    Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
    if and only if either (a == c and b == d), or (a == d and b == c) - that is,
    one domino can be rotated to be equal to another domino.

    Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is
    equivalent to dominoes[j].

    Constraints:
        1 <= dominoes.length <= 4 * 10^4
        dominoes[i].length == 2
        1 <= dominoes[i][j] <= 9
    """

    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        """
        Time complexity: O(N) - Beats 9.80%
        Space complexity: O(N) - Beats 43.47%

        Первое решение, ощущается как не оптимальное из-за преобразований
        """
        length = len(dominoes)
        counter = 0
        storage = Counter()
        for i in range(length):
            domino = tuple(dominoes[i])
            reversed_domino = tuple(reversed(domino))
            if domino in storage:
                storage[domino] += 1
            elif reversed_domino in storage:
                storage[reversed_domino] += 1
            else:
                storage[domino] = 1

        for value in storage.values():
            if value > 1:
                counter += value * (value - 1) / 2
        return int(counter)

    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        """
        Time complexity: O(N) - Beats 99.72%
        Space complexity: O(1) - Beats 43.47%

        Отличное решение: суть почти какая же, как в первом:
        Мы должны собирать домино с учетом возможной перестановки (val)
        Так как у нас есть ограничение 1 <= dominoes[i][j] <= 9, то мы не выйдем за пределы 100 чисел. (num)
        Считаем количество совпадений "на ходу": каждый раз прибавляем к результату текущее число таких же домино.
        Это эквивалент формуле n * (n - 1) / 2, но выполняется эффективнее.
        """
        num = [0] * 100
        result = 0
        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            result += num[val]
            num[val] += 1
        return result


# dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
s = Solution()
result = s.numEquivDominoPairs(dominoes)
print(result)
