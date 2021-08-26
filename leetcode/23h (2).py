# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = []
        if not lists:
            return None
        if not any(bool(l) for l in lists):  # all lists are empty
            return None

        q = PriorityQueue()
        while any(bool(l) for l in lists):
            for idx, l in enumerate(lists):
                if l:
                    q.put((l.val, random.random(), l))
                    lists[idx] = l.next

        output = []
        while not q.empty():
            _, _, node = q.get()
            output.append(node)

        for idx, node in enumerate(output):
            try:
                node.next = output[idx + 1]
            except IndexError:
                node.next = None
        return output[0]
