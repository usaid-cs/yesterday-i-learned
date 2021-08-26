# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recurse(node):
            if not node:
                new_node = TreeNode(val=val)
                return new_node
            if val < node.val:
                new_node = recurse(node.left)
                if new_node:
                    node.left = new_node
                    return
            elif val > node.val:
                new_node = recurse(node.right)
                if new_node:
                    node.right = new_node
                    return
        new_node = recurse(root)
        if new_node:
            return new_node
        return root
