class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            visited.add(head)
            child = head.next
            if child:
                if child in visited:
                    return True
            head = child
        return False