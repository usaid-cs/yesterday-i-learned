# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Eh:
    val = None
    left = None
    right = None
    parent = None

    def __init__(self):
        self.val = ''


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        s = '(' + s + ')'
        current_node = None
        root = current_node

        for idx, char in enumerate(s):
            # Process values
            if char.isdigit() or char == '-':
                current_node.val += char
                continue
            # Stack down
            if char == '(':
                new_node = Eh()
                new_node.parent = current_node
                if not current_node:
                    current_node = new_node
                    root = new_node
                elif not current_node.left:
                    current_node.left = new_node
                elif not current_node.right:
                    current_node.right = new_node
                else:
                    assert False
                current_node = new_node
            # Stack up
            elif char == ')':
                current_node = current_node.parent

        def recurse(node):
            if not node:
                return None
            new_node = TreeNode()
            new_node.val = node.val
            new_node.left = recurse(node.left)
            new_node.right = recurse(node.right)
            return new_node

        return recurse(root)
