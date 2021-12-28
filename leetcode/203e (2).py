# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        new_head = sentinel

        while new_head:
            next = new_head.next
            if not next:
                break
            if next.val == val:
                new_head.next = getattr(new_head.next, 'next', None)
            else:
                new_head = new_head.next
        return sentinel.next