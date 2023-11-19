from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Given the root of a binary tree, flatten the tree into a "linked list":

        The "linked list" should use the same TreeNode class where the right child pointer points
        to the next node in the list and the left child pointer is always null.
        The "linked list" should be in the same order as a pre-order traversal of the binary tree.

        Do not return anything, modify root in-place instead.
        """

        def preorder_traversal(node: TreeNode | None):
            if not node:
                return
            preorder_list.append(node.val)
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        preorder_list = []
        preorder_traversal(root)
        if preorder_list:
            root.left = None
            prev = root
            for val in preorder_list[1:]:
                node = TreeNode(val=val, left=None, right=None)
                prev.right = node
                prev = node

s = Solution()
r = s.flatten(
    root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))),
)
print(r)

class Solution2:
    """"""
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


class Solution3:
    """
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/1208004/extremely-intuitive-o-1-space-solution-with-simple-explanation-python/
    """
    def flatten(self, root: TreeNode) -> None:
        """
        Изначально будем перебирать все ноды, и если в них есть левая часть,
        то будем выполнять наш алгоритм:
        Суть: переносим правую ноду в последнюю правую левой ноды.
        Затем переносится вся левая нода в право, и идёт смещение на одну позицию под root (current),
        так как прошлая root нас уже не интересует
        """
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right

                cur.right = cur.left
                cur.left = None

            cur = cur.right
