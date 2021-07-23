# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def min_depth(node, current_level):
            if not node:
                return current_level
            if not (node.left or node.right):
                return current_level + 1

            left_min = 999999
            if node.left:
                left_min = min_depth(node.left, current_level + 1)
            right_min = 999999
            if node.right:
                right_min = min_depth(node.right, current_level + 1)
            return min(left_min, right_min)

        return min_depth(root, 0)
