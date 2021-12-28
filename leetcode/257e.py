"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        q = [(root, [root])]

        while q:
            node, nodes = q.pop(0)
            if not node:
                continue
            if not (node.left or node.right):
                paths.append(nodes)
                continue
            q.append((node.left, nodes + [node.left]))
            q.append((node.right, nodes + [node.right]))

        for idx, path in enumerate(paths):
            paths[idx] = '->'.join([str(x.val) for x in path])

        return paths