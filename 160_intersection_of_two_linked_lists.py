from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    Grade[Easy]
    Topics[Hash Table, Linked List, Two Pointers]

    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
    If the two linked lists have no intersection at all, return null.

    For example, the following two linked lists begin to intersect at node c1:


    The test cases are generated such that there are no cycles anywhere in the entire linked structure.

    Note that the linked lists must retain their original structure after the function returns.

    Custom Judge:

    The inputs to the judge are given as follows (your program is not given these inputs):

    intersectVal - The value of the node where the intersection occurs.
    This is 0 if there is no intersected node.
    listA - The first linked list.
    listB - The second linked list.
    skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
    The judge will then create the linked structure based on these inputs and pass the two heads, headA and
    headB to your program. If you correctly return the intersected node, then your solution will be accepted.
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

    # the idea is if you switch head, the possible difference between length would be countered.
    # On the second traversal, they either hit or miss.
    # if they meet, pa or pb would be the node we are looking for,
    # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them
