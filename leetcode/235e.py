# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > q.val:
            p, q = q, p

        def recurse(node):
            if not node:
                return None

            if p.val <= node.val <= q.val:  # because node can be p or q
                return node
            if p.val >= node.val:
                return recurse(node.right)
            if q.val <= node.val:
                return recurse(node.left)

        return recurse(root)
