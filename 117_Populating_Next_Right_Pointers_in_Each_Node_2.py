from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Populate each next pointer to point to its next right node. If there is no next right node,
    the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

    As the problem states that the output should return a tree with all the nodes in the same level connected,
    the problem can be solved using Level Order Traversal.
    Each iteration of Queue traversal, the code would:

    Find the length of the current level of the tree.
    Iterate through all the nodes in the same level using the level length.
    Find the siblings in the next level and connect them using next pointers. Enqueue all the nodes in the next level.

    Time = O(N) - iterate through all the nodes
    Space=O(L) - As the code is using level order traversal, the maximum size of Queue is maximum number
    of nodes at any level.
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        dummy = Node(-999)  # to initialize with a not null prev
        while q:
            length = len(q)  # find level length
            prev = dummy
            for _ in range(length):  # iterate through all nodes in the same level
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                    prev.next = popped.left
                    prev = prev.next
                if popped.right:
                    q.append(popped.right)
                    prev.next = popped.right
                    prev = prev.next
        return root


class Solution2:
    """
    In addition to this, there is a follow-up question asking to solve this problem using constant extra space.
    There is an additional hint to maybe use recursion for this and the extra call stack is assumed to be O(1) space

    The code will track the head at each level and use that not null head to define the next iteration.
    Following is my take on O(1) space solution:

    Time = O(N) - iterate through all the nodes
    Space = O(1) - No additional space
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        curr = root
        dummy = Node(-999)
        head = root

        while head:
            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal
            # iterate through the linked-list of the current level and connect all the siblings in the next level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node
        return root
