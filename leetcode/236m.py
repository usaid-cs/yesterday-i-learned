# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurse(node, find, parents):
            if not node:
                return
            if node is find:
                return parents + [node]
            left = recurse(node.left, find, parents + [node])
            if left:
                return left
            right = recurse(node.right, find, parents + [node])
            if right:
                return right
            return None

        p_path = recurse(root, p, [])
        assert p_path
        q_path = recurse(root, q, [])
        assert q_path

        long, short = p_path, q_path
        if len(p_path) < len(q_path):
            short, long = p_path, q_path

        for _ in range(len(long) - len(short)):
            long.pop()

        while long and short:
            l = long.pop()  # pop from the bottom because you're looking for the [L]CA
            if l is short.pop():
                return l

        return None
