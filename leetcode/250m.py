# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        univalue_subtrees = 0

        def all_values_are_the_same(node, needs_to_be):
            if not node:
                return True
            if node.val != needs_to_be:
                return False
            if not all_values_are_the_same(node.left, needs_to_be):
                return False
            return all_values_are_the_same(node.right, needs_to_be)

        def recurse(node):
            nonlocal univalue_subtrees
            if not node:
                return
            if all_values_are_the_same(node.left, node.val) and \
                    all_values_are_the_same(node.right, node.val):
                univalue_subtrees += 1
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        return univalue_subtrees
