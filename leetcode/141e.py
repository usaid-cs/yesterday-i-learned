# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while True:
            if not (slow or fast):
                return False
            slow = getattr(slow, 'next', None)
            fast = getattr(getattr(fast, 'next', None), 'next', None)
            if fast is slow and slow is not None:
                return True
