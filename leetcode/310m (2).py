"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
# this brute force solution will NOT pass leetcode
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        nodes = set()
        visited = set()

        for from_node, to_node in edges:
            nodes.add(from_node)
            nodes.add(to_node)
            graph[to_node].add(from_node)
            graph[from_node].add(to_node)

        def max_depth(node, d):
            if node in visited:
                return 0
            visited.add(node)
            depths = max(max_depth(child, d) for child in graph[node])
            return 1 + depths

        depths = {}
        for starting_node in sorted(list(nodes)):
            visited = set()
            depths[starting_node] = max_depth(starting_node, 0)

        if not depths:
            return [0]
        min_depth = min(depths.values())
        return [k for k, v in depths.items() if v == min_depth]
