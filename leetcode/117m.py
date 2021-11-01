"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = {

        }

        def recurse(node, level=0):
            if level not in q:
                q[level] = []
            if not node:
                return
            q[level].append(node)
            recurse(node.left, level + 1)
            recurse(node.right, level + 1)

        recurse(root)

        for level, nodes in q.items():
            for idx, node in enumerate(nodes):
                try:
                    node.next = nodes[idx + 1]
                except IndexError:
                    pass

        return root