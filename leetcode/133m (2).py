"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# BFS
class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        nodes = {}
        visited = set()

        q = [root]
        while q:
            node = q.pop(0)
            if not node:
                continue
            nodes[node] = []
            visited.add(node)
            for neighbor in node.neighbors:
                nodes[node].append(neighbor)
                if neighbor not in visited:
                    q.append(neighbor)

        new_nodes = {}
        for node, neighbors in nodes.items():
            new_nodes[node.val] = Node(val=node.val)

        for node, neighbors in nodes.items():
            new_neighbor_nodes = [node for val, node in new_nodes.items()
                                  if val in [n.val for n in neighbors]]
            new_nodes[node.val].neighbors = new_neighbor_nodes

        # print(new_nodes)
        for key in new_nodes:
            return new_nodes[key]
        return None
