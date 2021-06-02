class Node:
    def __init__(self):
        self.left = None
        self.right = None


def height(root):
    return get_layers(root) - 1


def get_layers(root):
    if not root:
        return 0
    return max(
        get_layers(root.left),
        get_layers(root.right)) + 1


one = Node()

two = Node()
two.left = one

four = Node()

seven = Node()

six = Node()
six.right = seven

five = Node()
five.left = four
five.right = six

three = Node()
three.left = two
three.right = five

fifteen = Node()


print(height(three))
print(height(fifteen))
