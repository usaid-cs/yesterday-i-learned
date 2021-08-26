"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        nodes = []

        def recurse(node):
            if not node:
                return
            while node:
                nodes.append(node)
                if node.child:
                    recurse(node.child)
                node = node.next

        recurse(head)
        print([node.val for node in nodes])

        for idx, node in enumerate(nodes):
            node.child = None
            try:
                next_node = nodes[idx + 1]
                next_node.prev = node
                node.next = next_node
            except IndexError:
                node.next = None
        if not nodes:
            return None
        return nodes[0]
