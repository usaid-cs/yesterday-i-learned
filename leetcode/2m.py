# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8 Explanation: 342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def add(node1, node2, carry_=0):
            next1 = None
            next2 = None
            if node1:
                val1 = node1.val
                next1 = node1.next
            else:
                val1 = 0
            if node2:
                val2 = node2.val
                next2 = node2.next
            else:
                val2 = 0

            if val1 + val2 + carry_ >= 10:
                carry = 1
                val = val1 + val2 + carry_ - 10
            else:
                carry = 0
                val = val1 + val2 + carry_
            node = ListNode(val)
            if next1 or next2:
                node.next = add(next1, next2, carry)
            elif carry:
                node.next = ListNode(1)
            return node

        return add(l1, l2)


list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(9)

a = Solution()
list3 = a.addTwoNumbers(list1, list2)
while list3:
    print(list3.val)
    list3 = list3.next