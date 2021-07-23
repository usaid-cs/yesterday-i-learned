# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        buffer = []

        def recurse(node):
            if not node:
                return
            buffer.append(node.val)
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        return buffer
