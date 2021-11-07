# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def recurse(node):
            nonlocal ans
            if not node:
                return False
            mid = node in [p, q]
            left = recurse(node.left)
            right = recurse(node.right)
            if (mid + left + right) >= 2:
                ans = node
            return mid or left or right

        recurse(root)
        return ans
