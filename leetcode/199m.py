# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        side_view = [None] * 100

        def recurse(node, level=0):
            if not node:
                return
            side_view[level] = node.val
            recurse(node.left, level + 1)
            recurse(node.right, level + 1)

        recurse(root)
        return [x for x in side_view if x is not None]
