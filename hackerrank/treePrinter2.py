class TreePrinter:
    def __init__(self):
        self.nodes = {}

    def add(self, parent, child):
        if parent in self.nodes:
            self.nodes[parent].append(child)
        else:
            self.nodes[parent] = [child]

    def get_root(self):
        """Who said this tree has only one root?

        Who said the tree is not cyclical because some
        people are crazy?
        """
        parents = set()
        children = set()
        for node, children_ in self.nodes.items():
            parents.add(node)
            for child_ in children_:
                children.add(child_)
        # A root node will never appear as a child.
        node_name = list(parents - children)[0]
        return node_name

    def get_children(self, node_name):
        if node_name in self.nodes:
            return self.nodes[node_name]
        return []

    def printTree(self, root_node=None, level=0):
        if root_node is None:
            root_node = self.get_root()
        if not root_node:
            return
        print('  ' * level + root_node)
        for child in self.get_children(root_node):
            self.printTree(root_node=child, level=level + 1)


a = TreePrinter()
a.add("animal", "mammal")
a.add("animal", "bird")
a.add("lifeform", "animal")
a.add("cat", "lion")
a.add("mammal", "cat")
a.add("animal", "fish")
a.printTree()
