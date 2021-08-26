class ThatSetThing:
    nodes = None  # values are roots

    def __init__(self, size):
        self.nodes = [0] * size
        for idx in range(size):
            self.nodes[idx] = idx  # Every node starts off as its own root

    def find_root(self, node):
        if self.nodes[node] == node:
            # It is a root
            return node
        return self.find_root(self.nodes[node])

    def union(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        self.nodes[root2] = root1  # join second branch with root

    def is_connected(self, node1, node2):
        return self.find_root(node1) == self.find_root(node2)

    def num_roots(self):
        roots = set()
        for node in self.nodes:
            node_root = self.find_root(node)
            roots.add(node_root)
        return len(roots)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_nodes = len(isConnected)
        set_thing = ThatSetThing(num_nodes)
        for node, connected_tos in enumerate(isConnected):
            for to_node, connected_to in enumerate(connected_tos):
                if connected_to == 1:
                    set_thing.union(node, to_node)

        return set_thing.num_roots()
