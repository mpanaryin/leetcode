from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Grade[Easy]
    Topics[Linked List]

    Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
    Return the linked list sorted as well.
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        current = head
        prev = None
        while current:
            if prev and prev.val == current.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return head
