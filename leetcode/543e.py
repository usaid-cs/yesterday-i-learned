# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_level = 0

        def max_depth(node, level):
            if not node:
                return level
            return max(
                max_depth(node.left, level + 1),
                max_depth(node.right, level + 1)
            )

        def recurse(node):
            nonlocal max_level
            if not node:
                return
            max_level = max(
                max_level,
                max_depth(node.left, 0) + max_depth(node.right, 0)
            )
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        return max_level
