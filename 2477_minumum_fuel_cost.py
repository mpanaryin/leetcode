import math
from collections import defaultdict
from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Tree, Depth-First Search, Breadth-First Search, Graph]

    There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of
    n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer
    array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
    There is a meeting for the representatives of each city. The meeting is in the capital city.
    There is a car in each city. You are given an integer seats that indicates the number of seats in each car.
    A representative can use the car in their city to travel or change the car and ride with another representative.
    The cost of traveling between two cities is one liter of fuel.
    Return the minimum number of liters of fuel to reach the capital city.
    """

    def minimum_fuel_cost(self, roads: List[List[int]], seats: int) -> int:
        self.edges = defaultdict(list)
        self.seats = seats
        self.fuel = 0
        for road in roads:
            self.edges[road[0]].append(road[1])
            self.edges[road[1]].append(road[0])

        def dfs(node, parent, edges, seats):
            representatives = 1
            for child in edges[node]:
                # Если ребенок не родитель
                if child != parent:
                    # Увеличиваем кол-во представителей в городах,
                    # с учетом кол-ва прошедших городов
                    representatives += dfs(child, node, edges, seats)
            # Расчёт, исключая нулевой узел
            if node != 0:
                self.fuel += math.ceil(representatives / seats)
            return representatives

        # Начинаем с 0, родители отсутствуют
        dfs(0, -1, self.edges, seats)
        return self.fuel
