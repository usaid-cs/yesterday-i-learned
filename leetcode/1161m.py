# "Should have done BFS"


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left.left = node4
node1.left.right = node5
node1.right.left = node6
node1.right.right = node7
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(14)
node15 = TreeNode(15)
node1.left.left.left = node8
node1.left.left.right = node9
node1.left.right.left = node10
node1.left.right.right = node11
node1.right.left.left = node12
node1.right.left.right = node13
node1.right.right.left = node14
node1.right.right.right = node15


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = [float('-inf')] * 10000

        def loop(node, level):
            if not node:
                return
            levels[level] += node.val
            loop(node.left, level + 1)
            loop(node.right, level + 1)

        loop(root, 1)
        max_level = 0
        max_val = float('-inf')
        for level, val in enumerate(levels):
            if val > max_val:
                max_level = level
                max_val = val
        return max_level


a = Solution()
a.maxLevelSum(node1)