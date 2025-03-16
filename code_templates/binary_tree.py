from collections import deque


def dfs(root):
    """
    Binary tree: DFS (recursive)
    """
    if not root:
        return
    ans = 0
    # do logic
    dfs(root.left)
    dfs(root.right)
    return ans


def dfs(root):
    """
    Binary tree: DFS (iterative)
    """
    stack = [root]
    ans = 0
    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans


def fn(root):
    """
    Binary tree: BFS
    """
    queue = deque([root])
    ans = 0
    while queue:
        current_length = len(queue)
        # do logic for current level
        for _ in range(current_length):
            node = queue.popleft()
            # do logic
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
