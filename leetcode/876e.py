# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = head
        node2 = head

        if not head:
            return head
        while True:
            try:
                node2 = node2.next.next
            except AttributeError:
                break
            node1 = node1.next
        return node1
