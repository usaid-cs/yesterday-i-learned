# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]
        while queue:
            p_head, q_head = queue.pop(0)
            if not (p_head or q_head):
                continue
            if not (p_head and q_head):
                return False
            if p_head.val != q_head.val:
                return False
            queue.append((p_head.left, q_head.left))
            queue.append((p_head.right, q_head.right))

        return not queue
