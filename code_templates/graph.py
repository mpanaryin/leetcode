from collections import deque

START_NODE = object

def fn(graph):
    """
    Graph: DFS (recursive)

    For the graph templates, assume the nodes are numbered from 0 to n - 1 and the graph is given as an adjacency list.
    Depending on the problem, you may need to convert the input into an equivalent adjacency list before using the
    templates.
    """
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)

        return ans
    seen = {START_NODE}
    return dfs(START_NODE)


def fn(graph):
    """
    Graph: DFS (iterative)
    """
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0
    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return ans


def fn(graph):
    """
    Graph: BFS
    """
    queue = deque([START_NODE])
    seen = {START_NODE}
    ans = 0
    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return ans
