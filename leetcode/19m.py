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


a = list_to_linked_list([1, 2, 3])
assert a.val == 1
assert a.next.val == 2
assert a.next.next.val == 3
assert a.next.next.next == None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        heads = []
        orig = head
        while head:
            heads.append(head)
            head = head.next
        for idx, node in enumerate(heads):
            if idx == len(heads) - n:
                if node.next:
                    node.val = node.next.val
                    node.next = node.next.next
                elif len(heads) == 1:
                    # Edge case removing the one-element list entirely
                    return None
                else:
                    heads[idx - 1].next = None
        return orig


a = Solution()
b = list_to_linked_list([1, 2, 3, 4, 5])
b = a.removeNthFromEnd(b, 2)
assert b.val == 1
assert b.next.val == 2
assert b.next.next.val == 3
assert b.next.next.next.val == 5

b = list_to_linked_list([1])
b = a.removeNthFromEnd(b, 1)
assert b is None