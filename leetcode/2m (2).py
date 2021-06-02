# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ll_to_list(self, ll):
        output = []
        while ll:
            output.append(ll.val)
            ll = ll.next
        return output

    def ll_to_int(self, ll):
        """Note: the linked list is reversed"""
        power = 0
        cum = 0
        num_list = self.ll_to_list(ll)
        for num in num_list:
            cum += num * pow(10, power)
            power += 1
        return cum

    def int_to_ll(self, num):
        """Note: the output must also be reversed"""
        if num <= 0:
            return ListNode(val=0)
        digits = reversed([x for x in str(num)])
        head = None
        true_head = None
        for digit in digits:
            if head is None:
                head = ListNode(val=digit)
                true_head = head
            else:
                head.next = ListNode(val=digit)
                head = head.next
        return true_head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return ListNode()
        l1_int = self.ll_to_int(l1)
        l2_int = self.ll_to_int(l2)
        l3 = l1_int + l2_int
        return self.int_to_ll(l3)
