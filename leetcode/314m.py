"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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
                # nodes_at_y = sorted(ys_at_x[y_value], key=lambda x: x.val)
                nodes_at_y = ys_at_x[y_value]
                for node_at_y in nodes_at_y:
                    nodes_at_x.append(node_at_y.val)
            ans.append(nodes_at_x)
        return ans
