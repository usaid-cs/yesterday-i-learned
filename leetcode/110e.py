# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def height(node, level=0):
            if not node:
                return level
            return max(height(node.left, level=level + 1),
                      height(node.right, level=level + 1))

        def recurse(node):
            if not node:
                return True
            if abs(height(node.left) - height(node.right)) > 1:
                return False
            return recurse(node.left) and recurse(node.right)

        return recurse(root)
