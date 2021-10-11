# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        candidates = []
        def recurse(node):
            if not node:
                return
            candidates.append((node.val, abs(abs(target) - abs(node.val))))
            recurse(node.left)
            recurse(node.right)            
        
        recurse(root)
        return list(sorted(candidates, key=lambda x: x[1]))[0][0]
