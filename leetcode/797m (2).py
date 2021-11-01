"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
# (BFS)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node = len(graph) - 1
        q = [[0]]
        ans = []

        while q:
            path = q.pop(0)
            last = path[-1]
            if last == last_node:
                ans.append(path)
            neighbors = graph[last]
            for neighbor in neighbors:
                if neighbor not in path:
                    q.append(path + [neighbor])

        return ans