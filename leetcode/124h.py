# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        current_max = float('-inf')

        node_cache = {}

        def max_sum_down(node):
            if not node:
                return 0
            if node in node_cache:
                return node_cache[node]

            computed = node.val + max(
                0,
                max_sum_down(node.left),
                max_sum_down(node.right))
            node_cache[node] = computed
            return computed

        def max_path_sum(node):
            nonlocal current_max

            if not node:
                return
            max_sum_left = max_sum_down(node.left)
            max_sum_right = max_sum_down(node.right)

            # Special case: also count root nodes with all negative children
            current_path_sum = node.val
            if current_path_sum > current_max:
                current_max = current_path_sum

            current_path_sum = max(0, max_sum_left) + max(0, max_sum_right) + node.val
            if current_path_sum > current_max:
                current_max = current_path_sum

            max_path_sum(node.left)
            max_path_sum(node.right)

        max_path_sum(root)
        return current_max
