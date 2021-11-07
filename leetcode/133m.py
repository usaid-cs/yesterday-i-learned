# The question said to use a stack. That's almost nonsense. DFS will do.

class Solution:

    cloned = None

    def cloneGraph(self, root: 'Node') -> 'Node':
        self.cloned = {}
        node = self.clone(root)
        # print(node, node.neighbors)
        return node

    def clone(self, node):
        if not node:
            return None
        if node.val in self.cloned:
            return self.cloned[node.val]

        new_node = Node(node.val)
        self.cloned[node.val] = new_node
        # print(node.neighbors)
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.clone(neighbor))
        return new_node
