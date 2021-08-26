# This solution times out, need to use a priority queue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = []
        if not lists:
            return None
        if not any(bool(l) for l in lists):  # all lists are empty
            return None

        while any(bool(l) for l in lists):
            min_list = None
            min_list_idx = None
            for idx, l in enumerate(lists):
                if l:
                    if min_list is None or l.val < min_list.val:
                        min_list = l
                        min_list_idx = idx
            lists[min_list_idx] = min_list.next
            output.append(min_list)

        for idx, node in enumerate(output):
            try:
                node.next = output[idx + 1]
            except IndexError:
                node.next = None
        return output[0]
