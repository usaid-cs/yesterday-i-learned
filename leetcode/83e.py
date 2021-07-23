# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(linked_list_to_list(self))


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


def linked_list_to_list(ll):
    l = []
    while ll:
        l.append(ll.val)
        ll = ll.next
    return l


def verify_linked_list(ll, l):
    while l:
        i = l[0]
        assert ll
        assert ll.val == i
        l.pop(0)
        ll = ll.next
    assert not ll, linked_list_to_list(ll)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        print(ptr)
        while ptr:
            print(ptr)
            nxt = ptr.next
            if not nxt:
                break
            val = nxt.val
            if ptr.val == val:
                ptr.next = nxt.next
                continue
            ptr = nxt

        return head


a = Solution()
sol = list_to_linked_list([])
verify_linked_list(a.deleteDuplicates(sol), [])
sol = list_to_linked_list([1,1,1])
verify_linked_list(a.deleteDuplicates(sol), [1])
sol = list_to_linked_list([1,2,3])
verify_linked_list(a.deleteDuplicates(sol), [1,2,3])
sol = list_to_linked_list([1,2,3,3,3,3,3,3,3])
verify_linked_list(a.deleteDuplicates(sol), [1,2,3])
