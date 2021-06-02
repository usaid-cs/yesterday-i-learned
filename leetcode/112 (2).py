class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def traverse(node, current_sum):
            if not node:
                return False
            if not (node.left or node.right):
                if node.val + current_sum == targetSum:
                    return True
            return traverse(node.left, node.val + current_sum) or \
                traverse(node.right, node.val + current_sum)
        return traverse(root, 0)
