# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = []
        def recurse(node):
            if not node:
                return
            vals.append(node.val)
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        vals.sort()
        vals2 = {}
        for idx, val in enumerate(vals):
            vals2[val] = idx
        for val, idx in vals2.items():
            if k - val in vals2:
                if vals2[k - val] != idx:
                    return True
        return False
