from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Breadth-First Search, Graph]

    You are given an integer n, the number of nodes in a directed graph where the nodes are labeled
    from 0 to n - 1.
    Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

    You are given two arrays redEdges and blueEdges where:
    redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to
    node bi in the graph, and
    blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
    Return an array answer of length n, where each answer[x] is the length of the shortest path
    from node 0 to node x such that the edge colors alternate along the path,
    or -1 if such a path does not exist.
    """

    def shortest_alternating_paths(self, N, red_edges, blue_edges) -> List[int]:
        """
        Time complexity: O(n + r + b)
        Space complexity: O(n + r + b)
        """
        adj_list = defaultdict(list)
        # Создаём словарь, в котором ключом является начальная позиция ребра,
        # а ключом конечная позиция ребра + цвет узла (0 - красный, 1 - синий)
        for u, v in red_edges: adj_list[u].append((v, 0))
        for u, v in blue_edges: adj_list[u].append((v, 1))
        # Создаем двустороннюю очередь с узлами и последним выбранным цветом. Начинаем с красного, потом синий
        queue = deque([(0, 0), (0, 1)])  # (node, last_color)

        dist = [float(inf)] * N
        visited = set()
        level = 0
        while queue:
            for _ in range(len(queue)):
                # Достаем узел и цвет
                node, last_color = queue.popleft()
                # Заполняем список узлом + минимальным значением по уровню узла
                # (уровень как раз равен числу шагов до него от нулевого элемента)
                dist[node] = min(dist[node], level)
                # Проходим по списку позиций ребра и их цветов, т.е. куда мы можем попасть из конкретного узла
                for nei, edge_color in adj_list[node]:
                    # Если последний выбранный цвет не совпадает с тем, который мы можем достать из этого узла и
                    # такая позиция узла с таким цветом не была ранее использована, то добавляем в посещенные и
                    # расширяем очередь
                    if last_color != edge_color and (nei, edge_color) not in visited:
                        visited.add((nei, edge_color))
                        queue.append((nei, edge_color))
            level += 1  # После прохода по всем возможным путям на текущем уровне переходим на следующий

        return [d if d != float(inf) else -1 for d in dist]  # Проходим наш список с узлами и результатами
