# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = None
        head = None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    if pointer is None:
                        pointer = l1
                        head = pointer
                    else:
                        pointer.next = l1
                    pointer = l1
                    l1 = l1.next
                else:
                    if pointer is None:
                        pointer = l2
                        head = pointer
                    else:
                        pointer.next = l2
                    pointer = l2
                    l2 = l2.next
            elif l1:
                if pointer is None:
                    pointer = l1
                    head = pointer
                else:
                    pointer.next = l1
                pointer = l1
                l1 = l1.next
            elif l2:
                if pointer is None:
                    pointer = l2
                    head = pointer
                else:
                    pointer.next = l2
                pointer = l2
                l2 = l2.next

        return head
