def fn(head):
    """
    Linked list: fast and slow pointer
    """
    slow = head
    fast = head
    ans = 0
    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next
    return ans


def fn(head):
    """
    Reversing a linked list
    """
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


