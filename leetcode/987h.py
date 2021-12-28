"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# It's a bit of a pointless question so don't do it if you're short on time
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = {}

        def recurse(node, y, x):
            if not node:
                return
            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = [node]
            else:
                nodes[x][y].append(node)
            recurse(node.left, y + 1, x - 1)
            recurse(node.right, y + 1, x + 1)

        recurse(root, 0, 0)

        ans = []
        x_values = sorted(nodes.keys())
        for x_value in x_values:
            nodes_at_x = []
            ys_at_x = nodes[x_value]
            y_values = sorted(ys_at_x.keys())
            for y_value in y_values:
                nodes_at_y = sorted(ys_at_x[y_value], key=lambda x: x.val)
                for node_at_y in nodes_at_y:
                    nodes_at_x.append(node_at_y.val)
            ans.append(nodes_at_x)
        return ans
