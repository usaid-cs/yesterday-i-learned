"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        levels = [[]]

        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            if not node:
                continue
            if level > len(levels) - 1:
                levels.append([])
            level_list = levels[level]
            level_list.append(node)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        for nodes_in_level in levels:
            for idx, node in enumerate(nodes_in_level):
                try:
                    node.next = nodes_in_level[idx + 1]
                except IndexError:
                    pass

        return root
