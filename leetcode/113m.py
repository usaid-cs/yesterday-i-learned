# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def recurse(node, path):
            if not node:
                return

            if not (node.left or node.right):
                if node.val + sum(path) == targetSum:
                    paths.append(path + [node.val])
            recurse(node.left, path + [node.val])
            recurse(node.right, path + [node.val])

        recurse(root, [])
        return paths
