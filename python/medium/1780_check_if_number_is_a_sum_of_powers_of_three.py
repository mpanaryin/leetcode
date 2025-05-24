import itertools


class Solution:
    """
    Grade[Medium]
    Topics[Math, Bit Manipulation, Simulation]

    Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three.
    Otherwise, return false.

    An integer y is a power of three if there exists an integer x such that y == 3x.

    Constraints:
    1 <= n <= 10^7
    """

    def checkPowersOfThree(self, n: int) -> bool:
        """
        Итоговая временная сложность:
            Построение списка numbers = O(log n)
            Генерация всех комбинаций = O(2^k) = O(n^(log3 2))
            Для каждой комбинации вычисление суммы: O(log n) на комбинацию
            Total time complexity: O(n^(log3 2) * log n)

        Пространственная сложность:
            Список numbers занимает O(log n) памяти.
            Список combinations содержит O(2^k) = O(n^(log3 2)) комбинаций, каждая из которых имеет длину O(log n)
            Total space complexity: O(n^(log3 2) * log n)
        """
        numbers = []
        power = 0
        number = 0
        while number < n:  # 10**7:
            number = 3 ** power
            numbers.append(number)
            power += 1
        combinations = [list(c) for r in range(1, len(numbers) + 1) for c in itertools.combinations(numbers, r)]
        all_possible_sums = set((sum(combination) for combination in combinations))
        return bool(n in all_possible_sums)


class Solution2:
    """
    Решение предложенное leetcode
    """

    def checkPowersOfThree(self, n: int) -> bool:
        return self._check_powers_of_three_helper(0, n)

    def _check_powers_of_three_helper(self, power: int, n: int) -> bool:
        # Base case: if n becomes 0, we have successfully formed the sum
        if n == 0:
            return True
        # If the current power of 3 exceeds n, we can't use it, so return false
        if 3 ** power > n:
            return False
        # Option 1: Include the current power of 3 and subtract it from n
        add_power = self._check_powers_of_three_helper(power + 1, n - 3 ** power)
        # Option 2: Skip the current power of 3 and try with the next power
        skip_power = self._check_powers_of_three_helper(power + 1, n)
        # Return true if either option leads to a valid solution
        return add_power or skip_power


s = Solution()
result = s.checkPowersOfThree(21)
print(result)
