# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        new_head = head
        while new_head:
            nodes.append(new_head)
            new_head = new_head.next
        
        new_head = head
        while new_head:
            the_other_head = nodes.pop()
            if new_head.val != the_other_head.val:
                return False
            new_head = new_head.next
        return True
