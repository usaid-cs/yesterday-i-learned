# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtree_hashes = {}

        def recurse(node):
            if not node:
                return None
            node_repl = (node.val, recurse(node.left), recurse(node.right))
            if node_repl in subtree_hashes:
                subtree_hashes[node_repl].append(node)
            else:
                subtree_hashes[node_repl] = [node]
            return node_repl

        recurse(root)
        return [y[0] for (x, y) in subtree_hashes.items()
                if x is not None and len(y) > 1]
