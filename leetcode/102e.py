# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = []

        def traverse(node, level):
            if not node:
                return
            if level > len(q) - 1:
                q.append([])
            q[level].append(node)
            traverse(node.left, level=level + 1)
            traverse(node.right, level=level + 1)

        traverse(root, level=0)
        vals = []
        for level in q:
            buffer = [x.val for x in level]
            vals.append(buffer)
        return vals
