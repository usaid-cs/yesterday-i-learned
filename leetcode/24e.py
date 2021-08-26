# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        def recurse(node):
            this_node = node
            if not this_node:
                return None
            that_node = this_node.next
            if not that_node:
                return this_node
            next_next_node = that_node.next
            this_node.next = recurse(next_next_node)
            that_node.next = this_node

            return that_node

        return recurse(head)
