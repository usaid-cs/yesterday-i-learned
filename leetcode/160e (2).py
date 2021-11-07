"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = 0
        len_b = 0

        node = headA
        while node:
            len_a += 1
            node = node.next

        node = headB
        while node:
            len_b += 1
            node = node.next

        if len_a <= len_b:
            long, short = headB, headA
        else:
            long, short = headA, headB

        for _ in range(abs(len_b - len_a)):
            long = long.next
        print(short.val, long.val)

        while long and short:
            if long == short:
                return long
            long = long.next
            short = short.next

        return None
