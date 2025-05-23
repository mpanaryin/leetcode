from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Grade[Medium]
    Topics[Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator]

    Implement the BSTIterator class that represents an iterator over the in-order traversal of
    a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
    The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent
    number smaller than any element in the BST.
    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
    otherwise returns false.
    int next() Moves the pointer to the right, then returns the number at the pointer.
    Notice that by initializing the pointer to a non-existent smallest number, the first call to next()
    will return the smallest element in the BST.

    You may assume that next() calls will always be valid. That is, there will be at least a next number in
    the in-order traversal when next() is called.

    Как по мне описание задачи сильно спутало. Прошлось написать обычный in_order_traversal,
    и придумать структуру, чтобы вытаскивать элементы в нужном порядке в соответствии задаче
    """

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur = root
        self.queue = self.set_queue()

    def set_queue(self):
        self.queue = deque([])
        self.in_order_traversal()
        return self.queue

    def in_order_traversal(self):
        def traverse(node):
            if node is not None:
                # Обход левого поддерева
                traverse(node.left)
                # Обработка текущего узла
                self.queue.append(node)
                # Обход правого поддерева
                traverse(node.right)

        traverse(self.root)

    def next(self) -> int:
        self.cur = self.queue.popleft()
        return self.cur.val

    def hasNext(self) -> bool:
        if self.queue:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
