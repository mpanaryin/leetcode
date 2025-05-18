# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    """
    Grade[Medium]
    Topics[Linked List, Two Pointers]

    Given the head of a linked list, rotate the list to the right by k places.
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        length = 0
        current = head
        last_node = None
        while current:
            if current.next is None:
                last_node = current
            current = current.next
            length += 1

        if length == k or length in [0, 1] or k == 0 or k % length ==0:
            return head
        elif length < k:
            min_rotate = k % length
        else:
            min_rotate = k

        current_index = 0
        current = head
        while True:
            current_index += 1
            prev = current
            current = current.next
            if current_index == length - min_rotate:
                prev.next = None
                last_node.next = head
                return current





linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
result = s.rotateRight(linked_list, 10)
print(result.val)