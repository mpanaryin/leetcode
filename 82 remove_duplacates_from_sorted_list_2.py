from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} | {self.next}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
        leaving only distinct numbers from the original list. Return the linked list sorted as well.

        Решение ужасное, надо будет изучить
        """
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



head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(5,))))))))
#head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3,)))))
head = ListNode(1, ListNode(1, ListNode(1, ListNode(2))))
head = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3)))))
s = Solution()
print(s.deleteDuplicates(head))