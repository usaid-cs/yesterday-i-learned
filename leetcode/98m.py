# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def is_valid(node, min_value, max_value):
            if not node:
                return True
            if node.val <= min_value:
                return False
            if node.val >= max_value:
                return False
            # min_value = max(node.val, min_value)
            # max_value = min(max_value, node.val)
            return (
                is_valid(node.left, min_value, min(max_value, node.val)) and
                is_valid(node.right, max(min_value, node.val), max_value))


        return is_valid(root, float('-inf'), float('inf'))
