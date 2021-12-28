# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        actual_head = ListNode(next=head)
        prev = None
        while head:
            if prev and head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return actual_head.next
