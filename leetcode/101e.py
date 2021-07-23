# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recurse(left_node, right_node):
            if not (left_node and right_node):
                if left_node or right_node:
                    return False
                return True
            if left_node.val != right_node.val:
                return False
            if not recurse(left_node.right, right_node.left):
                return False
            if not recurse(left_node.left, right_node.right):
                return False
            return True
        
        return recurse(root.left, root.right)
