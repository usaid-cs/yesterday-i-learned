# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            if not root.left:
                return None
            return self.searchBST(root.left, val=val)
        elif val > root.val:
            if not root.right:
                return None
            return self.searchBST(root.right, val=val)
        return None