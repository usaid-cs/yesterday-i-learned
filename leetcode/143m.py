# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        old_head = head
        while head:
            nodes.append(head)
            head = head.next

        nodes1 = [x for idx, x in enumerate(nodes) if idx < len(nodes) // 2]
        nodes2 = list(reversed([x for idx, x in enumerate(nodes) if idx >= len(nodes) // 2]))

        pointer = None
        # Push them in in pairs
        while nodes1 and nodes2:
            node1 = nodes1.pop(0)
            node2 = nodes2.pop(0)
            if pointer:
                pointer.next = node1
            else:
                pointer = node1
            node1.next = node2
            pointer = node2

        if nodes1:  # nodes1 is longer
            if pointer:
                pointer.next = nodes1[0]
                pointer.next.next = None
        elif nodes2:  # nodes2 is longer
            if pointer:
                pointer.next = nodes2[0]
                pointer.next.next = None
        else:
            if pointer:  # Pointer is None if
                pointer.next = None
