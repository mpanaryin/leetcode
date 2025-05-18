from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} | {self.next}"


class Solution:
    """
    Grade[Medium]
    Topics[Linked List, Two Pointers]

    Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list. Return the linked list sorted as well.

    Решение ужасное, надо будет изучить
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        dummy = ListNode(0, head)  # фиктивный узел перед головой
        prev = dummy
        current = head

        while current:
            # пропускаем все дубликаты
            if current.next and current.val == current.next.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
                prev.next = current  # пропустить дубликаты
            else:
                prev = current
                current = current.next

        return dummy.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        current = head
        prev = None
        last_deleted_value = None
        while current.next:
            if current.val == current.next.val:
                if prev:
                    prev.next = current.next.next
                else:
                    head = current.next.next

                last_deleted_value = current.val
                current = current.next.next
                if not current:
                    break
                continue
            elif current.val == last_deleted_value:
                if prev:
                    prev.next = current.next
                    current = current.next
                else:
                    head = current.next
                    current = current.next
                    if not current:
                        break
                continue
            prev = current
            current = current.next

        if current and current.val == last_deleted_value:
            if prev:
                prev.next = None
            else:
                return None
        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(5, ))))))))
# head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3,)))))
head = ListNode(1, ListNode(1, ListNode(1, ListNode(2))))
head = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3)))))
s = Solution()
print(s.deleteDuplicates(head))
