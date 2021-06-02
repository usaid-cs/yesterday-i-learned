# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        while head and head.val == val:
            head = head.next

        ptr = head
        while ptr:
            next = ptr.next
            if next and next.val == val:
                ptr.next = next.next
                continue
            ptr = next

        return head
