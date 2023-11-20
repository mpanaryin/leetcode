from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f'{self.val}'


class Solution:
    """
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
    The binary tree has the following definition:
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
    should be set to NULL.
    Initially, all next pointers are set to NULL.

    SOLUTION:
    Now, we need to populate next pointers of each node with nodes that occur to its immediate right on the same level.
    This can easily be done with BFS. Since for each node, we require the right node on the same level,
    we will perform a right-to-left BFS instead of the standard left-to-right BFS.

    Before starting the traversal of each level, we would initialize a rightNode variable set to NULL.
    Then, since we are performing right-to-left BFS, we would be starting at rightmost node of each level.
    We set the next node of cur as rightNode and update rightNode = cur. This would ensure that each node would be
    assigned its rightNode properly while traversing from right to left.
    Also, if cur has a child, we would first push its right child and only then its left child (since we are doing
    right-to-left BFS). Once BFS is completed (after queue becomes empty), all next node would be populated and
    we can finally return root.
    """
    def connect(self, root: Node):
        if not root:
            return None
        q = deque([root])  # Состоит из 1 элемента - root
        while q:
            right_node = None  # Возвращаемся сюда, после основного обхода q, чтобы обойти его extend
            for _ in range(len(q)):
                cur = q.popleft()  # Забираем первый элемент и удаляем его из очереди
                cur.next, right_node = right_node, cur  # Обход right -> left
                if cur.right:
                    q.extend([cur.right, cur.left])  # Дополняем q для обхода right -> left
        return root


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
s = Solution()
s.connect(root=root)
