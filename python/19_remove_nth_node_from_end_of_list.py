from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Grade[Medium]
    Topics[Linked List, Two Pointers]

    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Решение: создаём список всех значений. По индексу вырезаем ненужное число.
    После создаём связный список ListNode's
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        values_list = []
        self.get_values_list(head, values_list)
        values_list.pop(-n)
        list_length = len(values_list)
        values_list.reverse()
        i = 0
        node = None
        while i != list_length:
            node = ListNode(values_list[i], node)
            i += 1
        return node

    def get_values_list(self, head, values_list):
        """Получаем список всех значений"""
        if head is None:
            return
        values_list.append(head.val)
        self.get_values_list(head.next, values_list)

