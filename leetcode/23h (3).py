# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import random
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        sentinel = ListNode()
        q = PriorityQueue()

        # Store the heads of each list in a PQ.
        for lst in lists:
            if lst:
                q.put((lst.val, random(), lst))

        point = sentinel
        while not q.empty():
            val, _, node = q.get()
            point.next = ListNode(val)
            point = point.next
            if node.next:  # make the queue compare the list heads again
                q.put((node.next.val, random(), node.next))
        point.next = None
        return sentinel.next
