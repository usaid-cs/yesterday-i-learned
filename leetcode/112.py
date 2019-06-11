#!/usr/bin/env python3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: int) -> bool:
        def is_leaf(node):
            return node.left is None and node.right is None

        # The "fuck you" base cases (the problem doesn't even explain
        # the empty case so it's fucking undefined until you waste an
        # attempt solving it)
        if not root:
            return False
        if is_leaf(root):
            return root.val == sum

        def sums_up(base_value, sub_root):
            if not sub_root:
                return False
            val = sub_root.val
            if is_leaf(sub_root):
                if base_value + val == sum:
                    return True
            return sums_up(base_value + val, sub_root = sub_root.left) or \
             sums_up(base_value + val, sub_root = sub_root.right)

        return sums_up(root.val, sub_root=root.left) or \
             sums_up(root.val, sub_root=root.right)


runner = Solution()
assert runner.hasPathSum(None, 0)
assert runner.hasPathSum(None, 1) == False
assert runner.hasPathSum(TreeNode(), 1) == False