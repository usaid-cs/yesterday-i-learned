"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        nodes = defaultdict(list)

        def recurse(node):
            if not node:
                return
            if node.left:
                nodes[node].append(node.left)
                nodes[node.left].append(node)
                recurse(node.left)
            if node.right:
                nodes[node].append(node.right)
                nodes[node.right].append(node)
                recurse(node.right)

        recurse(root)
        q = [(target, 0)]
        visited = set()
        ans = []
        while q:
            node, distance = q.pop(0)
            if distance == k:
                ans.append(node.val)
            visited.add(node)
            neighbors = nodes[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append((neighbor, distance + 1))
        return ans
