from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Grade[Medium]
    Topics[Linked List, Math, Recursion]

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(max(n, m))
        Space complexity: O(max(n, m))
        """
        result = ListNode(0)

        def get_number(node1, node2, pointer_node, number=0, ten=0):
            if node1 or node2 or ten:
                num_1 = node1.val if node1 else 0
                num_2 = node2.val if node2 else 0

                number = num_1 + num_2 + ten
                ten = number // 10
                number = number % 10

                pointer_node.next = ListNode(number)
                pointer_node = pointer_node.next

                return get_number(
                    node1.next if node1 else None,
                    node2.next if node2 else None,
                    pointer_node,
                    number,
                    ten
                )
            return result.next

        return get_number(l1, l2, result)
