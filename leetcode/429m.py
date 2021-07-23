"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [(root, 0)]
        output = []

        if not root:
            return output

        while queue:
            node, level = queue.pop(0)

            if len(output) <= level:
                output.append([])
            level_lst = output[level]
            level_lst.append(node.val)

            for child in node.children:
                queue.append((child, level + 1))

        return output
