from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    def len(self):
        value = 1
        next: ListNode = self.next
        while next:
            value += 1
            next = next.next
        return value

    def get_list(self):
        lst = [self.val]
        index = 1
        next: ListNode = self.next
        while next:
            lst.append(next.val)
            index += 1
            next = next.next
        return lst


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, return the list after sorting it in ascending order.
        Сортировка слиянием
        """
        if not head or not head.next:
            return head
        # делим пополам
        middle = self.get_middle(head)
        left = head
        right = middle.next
        middle.next = None  # разрываем список на две половины
        # Проходим по всем элементам рекурсивно пока не дойдём до одного элемента в списке
        left = self.sortList(left)
        right = self.sortList(right)
        # Соединяем
        return self.merge(left, right)

    def get_middle(self, head: ListNode):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: ListNode, right: ListNode):
        dummy = ListNode()  # Вспомогательный узел для упрощения слияния
        tail = dummy
        # Слияние двух отсортированных списков
        while left and right:
            # Если элемент слева меньше правого, то первый элемент в хвосте становится левым
            # Сам левый элемент становится следующим у себя
            if left.val < right.val:
                tail.next = left
                left = left.next
            # Если левый больше, чем правый, то следующий в хвосте - это правый элемент,
            # а сам правый заменяется на следующим у себя
            else:
                tail.next = right
                right = right.next
            # После чего всегда переключаем хвост на только что добавленный в него элемент
            tail = tail.next
        # Присоединяем оставшуюся часть списка, когда остается 1 элемент (если он остается)
        tail.next = left if left else right
        return dummy.next


head1 = ListNode(4, ListNode(2, ListNode(5, ListNode(1, ListNode(3, ListNode(6, ListNode(7)))))))
head2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
head3 = ListNode(1, ListNode(1))
head4 = ListNode(3, ListNode(2, ListNode(4)))

s = Solution()
result = s.sortList(head1)
print(result.get_list())
