# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_linked_list(l):
    prev = None
    head = None
    for item in l:
        node = ListNode(item)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head


def verify_linked_list(ll, l):
    while l:
        i = l[0]
        assert ll
        assert ll.val == i
        l.pop(0)
        ll = ll.next
    assert not ll


a = list_to_linked_list([1, 2, 3, 4, 5])
verify_linked_list(a, [1, 2, 3, 4, 5])


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        def eh(parent, node):
            if not node.next:
                new_head = node
            node.next = parent
            return node

        return eh(None, head)