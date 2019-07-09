# "Removing" a linked list node involves copying the next node's value,
# and then skipping the next node. It does not involve actually removing
# the reference to the current node.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        node.val = node.next.val
        node.next = node.next.next