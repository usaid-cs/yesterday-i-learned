"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        def trees_match(node1, node2):
            if node1 == node2 == None:
                return True
            if not (node1 and node2):
                return False
            if node1.val != node2.val:
                return False
            return (
                    trees_match(node1.left, node2.left) and
                    trees_match(node1.right, node2.right)
            )

        def recurse(node):
            nonlocal ans
            if not node:
                return
            if trees_match(node, subRoot):
                ans = True
                return
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        return ans