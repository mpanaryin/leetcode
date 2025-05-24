from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Grade[Medium]
    Topics[Tree, Depth-First Search, Binary Search Tree, Binary Tree]

    You are given the root of a binary search tree (BST), where the values of exactly two nodes
    of the tree were swapped by mistake. Recover the tree without changing its structure.

    Do not return anything, modify root in-place instead.

    Этот код выполняет inorder обход дерева, при этом отслеживаются два узла first и second,
    которые нарушают порядок. После завершения обхода, их значения меняются местами,
    чтобы восстановить правильное дерево.

    Тут важно будет понимание рекурсии: обход сначала по левым ветвям, только дойдя до самого низа
    (изначально 1 элемент), мы начинаем перепрыгивать на правые ветви по одной наверх.
    """

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Time complexity: O(n)
        Space complexity: O(h)
        """

        def in_order_traversal(node: Optional[TreeNode]):
            nonlocal prev, first, second
            if node:
                in_order_traversal(node.left)
                if prev:
                    print(f"{node.val} < {prev.val}")
                if prev and node.val < prev.val:
                    print('prev: ', prev.val)
                    if not first:
                        first = prev
                    second = node
                prev = node
                in_order_traversal(node.right)

        prev = first = second = None
        in_order_traversal(root)

        # Swap the values of the first and second nodes to recover the tree
        first.val, second.val = second.val, first.val


def build_test_tree():
    # Создаем дерево с двумя перепутанными узлами
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(8, TreeNode(9), TreeNode(7)))
    return root


def print_tree_in_order(node):
    if node:
        print_tree_in_order(node.left)
        print(node.val, end=' ')
        print_tree_in_order(node.right)


# Создаем экземпляр Solution
solution = Solution()

# Строим дерево и выводим его до восстановления
root = build_test_tree()
print("Исходное дерево:")
print_tree_in_order(root)
print()

# Восстанавливаем дерево
solution.recoverTree(root)

# Выводим восстановленное дерево
print("Восстановленное дерево:")
print_tree_in_order(root)
