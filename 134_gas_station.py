class Solution:
    """
    Grade[Medium]
    Topics[Array, Greedy]

    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to
    its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index
    if you can travel around the circuit once in the clockwise direction,
    otherwise return -1. If there exists a solution, it is guaranteed to be unique

    Constraints:
        n == gas.length == cost.length
        1 <= n <= 10**5
        0 <= gas[i], cost[i] <= 10**4
    """
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def counter(start_index: int | None, length: int, current_tank: int):
            """Постоянный подсчёт, можем ли мы пройти круг с определенного значения"""
            for i in range(0 if start_index is None else start_index, length):
                if start_index is None and gas[i] >= cost[i]:
                    start_index = i
                    current_tank += gas[i] - cost[i]
                else:
                    current_tank += gas[i] - cost[i]
                    if current_tank < 0:
                        return counter(i+1, length, 0)
            # Если мы смогли пройти круг с первого элемента
            if start_index == 0 and length == len(gas):
                return start_index
            # Если мы смогли пройти круг не с первого элемента
            elif start_index == 0 and length != len(gas):
                return length
            # Если мы начали проходить круг не с первого элемента, но ещё не сломались и должны завершить начало
            else:
                return counter(0, start_index, current_tank)

        if sum(gas) < sum(cost):
            return -1
        return counter(None, len(gas), 0)

    def canCompleteCircuit2(self, gas: list[int], cost: list[int]) -> int:
        """
        Улучшенное решение, почти аналогичное моему.
        Просто тут необходимо заметить, что мы можем при единичном проходе не перепрыгивать в начало
        на i + 1 (как было в моём случае), где i - начало прохода от станции, где достаточно газа для первой поездки.
        А просто запоминать новое начало, отбрасывая весь предыдущий путь, так как там видимо уже нет хороших путей.
        """
        n, total_surplus, surplus, start = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start


# 1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
# 2
gas = [2, 3, 4]
cost = [3, 4, 3]
# 3
gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
# 4
gas = [2]
cost = [2]
s = Solution()
result = s.canCompleteCircuit(gas, cost)
print('result: ', result)