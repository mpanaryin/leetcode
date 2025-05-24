from collections import defaultdict


class Solution:
    """
    Grade[Medium]

    There are n types of units indexed from 0 to n - 1. You are given a 2D integer array conversions of length n - 1,
    where conversions[i] = [sourceUniti, targetUniti, conversionFactori].
    This indicates that a single unit of type sourceUniti is equivalent to conversionFactori units of type targetUniti.

    Return an array baseUnitConversion of length n, where baseUnitConversion[i] is the number of units of type
    i equivalent to a single unit of type 0. Since the answer may be large,
    return each baseUnitConversion[i] modulo 10^9 + 7.

    Constraints:
        2 <= n <= 10^5
        conversions.length == n - 1
        0 <= sourceUniti, targetUniti < n
        1 <= conversionFactori <= 10^9
    """
    MOD = 10 ** 9 + 7

    def baseUnitConversions(self, conversions: list[list[int]]) -> list[int]:
        # Определяем сколько всего типов единиц у нас есть
        n = 1 + max(
            max(source for source, _, _ in conversions),  # находит максимальный номер источника
            max(target for _, target, _ in conversions)  # находит максимальный номер цели
        )

        graph = defaultdict(list)  # граф переходов между единицами
        for source, target, factor in conversions:
            graph[source].append((target, factor))  # из source можно перейти в target с множителем factor.

        result = [0] * n
        result[0] = 1  # Базовая единица
        # Начиная от 0, мы рекурсивно вычисляем пересчёт для всех остальных единиц.
        self.dfs(0, graph, result)
        return result

    def dfs(
        self,
        node: int,
        graph: dict[int, list[tuple[int, int]]],
        result: list[int]
    ):
        for neighbor, factor in graph[node]:
            result[neighbor] = (result[node] * factor) % self.MOD
            self.dfs(neighbor, graph, result)
