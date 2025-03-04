from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def length(self):
        counter = 0
        current = self
        while current:
            counter += 1
            current = current.next
        return counter


class Solution:
    """
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
    """

    def get_head_length(self, head: Optional[ListNode]) -> int:
        counter = 0
        current = head
        while current:
            counter += 1
            current = current.next
        return counter

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity = O(n)
        Space complexity = O(1)
        """
        length = self.get_head_length(head)
        n = 0
        while n != length//2:
            head = head.next
            n += 1
        return head


head = ListNode(
    1, ListNode(
        2, ListNode(3)
    )
)

s = Solution()
result = s.middleNode(head)
print(result)

