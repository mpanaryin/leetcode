from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Binary Search]

    A conveyor belt has packages that must be shipped from one port to another within days days.

    The ith package on the conveyor belt has a weight of weights[i].
    Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
    We may not load more weight than the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in all the packages on the conveyor
    belt being shipped within days days.

    Решение через бинарный поиск
    """

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Time complexity: O(n * log(sum(weights) - max(weights)))
        Space complexity: O(1)
        """
        def feasible(capacity) -> bool:
            D = 1
            total = 0
            for weight in weights:
                total += weight
                # Если сумма весов преодолевает центр, то текущая сумма перебранных весов
                # будет равна последнему значению веса, так как на следующей итерации уже будет новый день
                # и прибавлять веса мы будем к нему
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    D += 1
                    if D > days:  # cannot ship within D days
                        return False
            return True

        # Левый - максимальный вес одной посылки. Будет расти, если нам не хватит дней
        # разместить все посылки в пределах этого веса.
        # Правый - сумма всех весов. Мы не можем превысить это значение.
        # Так как оно будет в случае отправки в 1 день
        left, right = max(weights), sum(weights)
        while left < right:
            # центр определяется как максимальный вес + (сумма весов - максимальный вес) // 2
            mid = left + (right - left) // 2  # Понять невозможно - просто это шаблон бинарного поиска
            if feasible(mid):
                # Если мы смогли пройти все веса, при этом не превысив лимит дней
                right = mid
            else:
                left = mid + 1
        return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

# weights = [3,2,2,4,1,4]
# days = 3


# weights = [1,2,3,1,1]
# days = 4

# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 10

# weights = [147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47]
# days = 10

s = Solution()
result = s.shipWithinDays(weights, days)
print(result)
