"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

#         depth = 0

#         def recurse(node, level):
#             nonlocal depth
#             if not node:
#                 return level
#             depth = max(depth, level)
#             for child in node.children:
#                 recurse(child, level + 1)

#         recurse(root, 1)
#         return depth
        depth = 0
        q = [(root, 1)]
        while q:
            node, level = q.pop(0)
            if not node:
                continue
            depth = max(depth, level)
            for child in node.children:
                q.append((child, level + 1))
        return depth
