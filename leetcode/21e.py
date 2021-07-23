# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        l1_cur = l1
        l2_cur = l2
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l1_cur = l1
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
                else:
                    l2_cur = l2
                    cur.next = l2
                    cur = l2
                    l2 = l2.next
            elif l1:
                l1_cur = l1
                cur.next = l1
                cur = l1
                l1 = l1.next
            elif l2:
                l2_cur = l2
                cur.next = l2
                cur = l2
                l2 = l2.next
                    
        return head.next
