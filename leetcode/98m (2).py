"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurse(node, local_min=float('-inf'), local_max=float('inf')):
            if not node:
                return True
            if not (local_min < node.val < local_max):
                return False
            return recurse(node.left, local_min, node.val) and recurse(node.right, node.val, local_max)

        return recurse(root)