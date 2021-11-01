# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def first_node_different(node):
            if not node:
                return False, None

            un_target = node.val

            items_removed = False
            while node.next:
                if node.next.val != un_target:
                    return items_removed, node.next
                else:
                    items_removed = True
                node = node.next
            return items_removed, None

        sentinel = ListNode(-1111111, head)
        node = sentinel
        prev = sentinel
        while node:
            items_removed, temp = first_node_different(node)
            if items_removed:
                prev.next = temp
                node = temp
            else:
                node.next = temp
                prev = node
                node = node.next
        return sentinel.next
