from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Grade[Easy]
    Topics[Linked List, Recursion]

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of
    the first two lists.

    Return the head of the merged linked list.

    Решение: создаём список всех значений. После сортируем, разворачиваем и
    создаём связный список ListNode's
    """
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n + m)
        Space complexity: O(n + m)
        """
        values_list1 = []
        values_list2 = []
        self.get_values_list(list1, values_list1)
        self.get_values_list(list2, values_list2)

        values_list1.extend(values_list2)
        values_list1.sort()
        values_list1.reverse()
        list_length = len(values_list1)
        i = 0
        node = None
        while i != list_length:
            node = ListNode(values_list1[i], node)
            i += 1
        return node

    def get_values_list(self, head, values_list):
        """Получаем список всех значений"""
        if head is None:
            return
        values_list.append(head.val)
        self.get_values_list(head.next, values_list)


class Solution2:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() # Сначала они все ссылаются на один и тот же пустой узел
        while list1 and list2:
            if list1.val < list2.val: # если значение в первом списке меньше
                # Назначаем текущему списку next элемент равным list1.
                # Dummy тоже будет назначен этот элемент
                cur.next = list1
                # Тут мы смещаем list1 на один элемент.
                # Текущий список становится равным list1 и теряет связь с dummy.
                list1, cur = list1.next, list1 # смещаем list1 на один элемент,
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next

