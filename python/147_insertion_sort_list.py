from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def len(self):
        value = 1
        next: ListNode = self.next
        while next:
            value += 1
            next = next.next
        return value

    def __repr__(self):
        return str(self.val)

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
    """
    Grade[Medium]
    Topics[Linked List, Sorting]

    Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

    The steps of the insertion sort algorithm:

    1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    2. At each iteration, insertion sort removes one element from the input data,
    finds the location it belongs within the sorted list and inserts it there.
    3. It repeats until no input elements remain.

    The following is a graphical example of the insertion sort algorithm.
    The partially sorted list (black) initially contains only the first element in the list.
    One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

    Constraints:
    The number of nodes in the list is in the range [1, 5000].
    -5000 <= Node.val <= 5000
    """

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Написано лично мной с попыткой собственного осознания каждого шага. Решение не совсем оптимальное.
        Моя логика была такая: удаляем элемент на текущей итерации и ищем куда мы его можем вставить итерируясь
        заново по списку до текущего индекса. Если не нашли куда вставить, вставляем обратно на свою позицию.
        """
        def recursion(head: ListNode, check_index: int):
            current_index = 0
            prev = None
            current_node = head
            while current_index != list_length:
                if check_index == current_index:
                    # remove_and_insert
                    # removed
                    prev.next = current_node.next
                    # insert
                    head, _ = self._insert(head, current_node, current_index + 1)
                    return recursion(head, check_index + 1)

                prev = current_node
                current_node = current_node.next
                current_index += 1
            return head

        list_length = self._list_length(head)
        return recursion(head, 1)


    def _list_length(self, head: ListNode):
        value = 1
        next: ListNode = head.next
        while next:
            value += 1
            next = next.next
        return value

    def _insert(self, head: ListNode, inserted_node: ListNode, inserted_node_index: int) -> tuple[ListNode, ListNode]:
        index = 1
        previous_node = None
        current_node = head
        while current_node:
            if inserted_node.val <= current_node.val or inserted_node_index == index:
                # Создаём связь с предыдущим узлом, если он был
                if previous_node:
                    previous_node.next = inserted_node
                # Делаем вставку
                inserted_node.next = current_node
                # Если вставили сразу в начало
                if index == 1:
                    return inserted_node, inserted_node
                # Если вставили не в начало
                return head, inserted_node
            index += 1
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = inserted_node
        inserted_node.next = None
        return head, inserted_node

    def insertionSortList2(self, head: ListNode | None) -> ListNode | None:
        """Ещё одно решение, которое я попытался реализовать самостоятельно"""
        self._swapper(head)
        return head

    def _swapper(self, node: ListNode | None) -> ListNode | None:
        if node is None:
            return
        # Текущий нод, который мы будем свапать с другими по значениям
        dummy = node
        # Нужно запомнить какой нод был в самом начале, чтобы узнать потом, изменилось ли его значение
        start_node = node
        # Запоминаем значение начального нода, так как оно может измениться
        start_value = node.val
        # Итерируемся по всем элементам
        while node.next:
            # Если изучаемый нами элемент больше элемента в списке, их нужно свапать
            if dummy.val > node.next.val:
                # Свапаем значения и запоминаем новое положение нашего текущего значения
                dummy.val, node.next.val = node.next.val, dummy.val
                dummy = node.next
            node = node.next
        return self._swapper(start_node.next if start_node.val == start_value else start_node)

    def insertionSortList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Взято из решений, выглядит неплохо, легко для понимания.
        Чем-то похоже на два указателя: мы одновременно итерируемся по двум спискам,
        заменяя значения в порядке сортировки.
        Основной список проходим по каждому элементу, вложенный список догоняет основной список.
        """
        current_node = head
        # Проходимся по всем элементам связного списка
        while current_node:
            wrapped_node = head
            # Начинаем проходить по тому же списку пока не дойдём до текущего элемента
            while wrapped_node != current_node:
                # Если есть значение, которое встречается в списке раньше и оно больше текущего,
                # то мы меняем их местами
                if wrapped_node.val > current_node.val:
                    wrapped_node.val, current_node.val = current_node.val, wrapped_node.val
                wrapped_node = wrapped_node.next
            current_node = current_node.next
        return head

    def insertionSortList4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Лучшее решение. Самое быстрое, но труднее для понимания
        """
        # Создаём "куклу", которая всегда будет знать о head.
        # Итерацию начинаем со второго элемента, поэтому предыдущим изначально считаем head
        dummy, cur_prev, cur = ListNode(-1, head), head, head.next
        while cur:
            # Запоминаем текущий порядок следования элементов
            # j_prev - несуществующая нода, которую мы добавили
            # j - первый существующий элемент, по сути head всего списка на текущей итерации
            # cur_next - следующий элемент в списке на текущей итерации
            j_prev, j, cur_next = dummy, dummy.next, cur.next
            print('j_prev, j, cur_next: ', j_prev, j, cur_next)
            # Если значение у текущего больше, чем значение у предыдущего,
            # то предыдущий элемент становится текущим, так как мы двигаемся по списку, а тут нечего менять
            if cur.val > cur_prev.val:
                cur_prev = cur
                print('cur.val > cur_prev.val: ', cur_prev)
            # В ином случае мы итерируемся по всем элементам списка, пока не дойдём до текущего.
            # При этом на каждой итерации мы делаем перестановку таким образом,
            # чтобы j оставался самым большим элементом перед текущим, чтобы сделать перестановку этих элементов
            else:
                print('while j.val < cur.val: ', j.val, '<', cur.val)
                while j.val < cur.val:
                    print('j, j.next: ', j, j.next)
                    j_prev, j = j, j.next
                # Следующий у текущего становится j, который в свою очередь является э
                # чуть больше или равным по значению для текущего. Т.е. текущий не может быть меньше j.
                cur.next = j
                # j_prev становится тем элементом, который мы только что проверяли
                j_prev.next = cur
                # следующий у предыдущего становится текущий-следующий
                cur_prev.next = cur_next
                print('cur.next = j: ', cur.next)
                print('j_prev.next = cur: ', j_prev.next)
                print('cur_prev.next = cur_next', cur_prev.next)
            cur = cur_next
            print('cur: ', cur)
            print(dummy.get_list())
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
        return dummy.next


node1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
node2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
node3 = ListNode(1, ListNode(1))
node4 = ListNode(3, ListNode(2, ListNode(4)))
# print(node.get_list())
# print(node.len())
s = Solution()
result = s.insertionSortList3(node1)
print(result.get_list())
