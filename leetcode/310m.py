"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
# this brute force solution will NOT pass leetcode
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # use a set to track the nodes you've already visited

        depths = []  # [(depth, starting_node), ...]
        graph = {}

        for edge in edges:
            left, right = edge
            if left in graph:
                graph[left].append(right)
            else:
                graph[left] = [right]
            if right in graph:
                graph[right].append(left)
            else:
                graph[right] = [left]

        for starting_node in graph:
            visited = set()
            depth = 0
            q = [(starting_node, 1)]  # second value is depth
            while q:
                num, depth_here = q.pop(0)
                depth = max(depth, depth_here)
                visited.add(num)
                children = graph[num]
                for child in children:
                    if child not in visited:
                        q.append((child, depth_here + 1))
            depths.append((depth, starting_node))

        depths.sort(key=lambda x: x[0])
        if not depths:
            return [0]
        min_depth = depths[0][0]
        return [d[1] for d in depths if d[0] == min_depth]
