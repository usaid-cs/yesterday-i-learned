# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def recurse(node, current_sum):
            if not node:
                return False
            if (current_sum + node.val) == targetSum:
                if not (node.left or node.right):
                    return True
            return recurse(node.left, current_sum + node.val) or recurse(node.right, current_sum + node.val)

        if not root:
            return False
        return recurse(root, 0)