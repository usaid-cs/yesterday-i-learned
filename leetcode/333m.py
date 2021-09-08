# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        stack = []
        subtree_size_map = {}  # node: how big
        subtree_minmax_map = {}  # node: (min, max)
        is_bst_map = {}  # node: bool

        def is_bst(node):
            if node in is_bst_map:
                # Cache
                return is_bst_map[node]
            if not node:
                # Because you recurse and need to find out
                return True

            if not (is_bst(node.left) and is_bst(node.right)):
                # Subtrees aren't BSTs so nor am I
                is_bst_map[node] = False
                subtree_size_map[node] = 0
                subtree_minmax_map[node] = [node.val, node.val]
                return is_bst_map[node]

            if node.left and node.right:
                is_bst_ = (
                    node.left.val < node.val < node.right.val
                    and subtree_minmax_map[node.left][0] < node.val
                    and subtree_minmax_map[node.left][1] < node.val
                    and subtree_minmax_map[node.right][0] > node.val
                    and subtree_minmax_map[node.right][1] > node.val
                )
                is_bst_map[node] = is_bst_
                if is_bst_:
                    subtree_size_map[node] = subtree_size_map[node.left] + subtree_size_map[node.right] + 1
                    subtree_minmax_map[node] = [subtree_minmax_map[node.left][0], subtree_minmax_map[node.right][1]]
                else:
                    subtree_size_map[node] = 0
                    subtree_minmax_map[node] = [node.val, node.val]
                return is_bst_
            if node.left:
                is_bst_ = (
                    node.left.val < node.val
                    and subtree_minmax_map[node.left][0] < node.val
                    and subtree_minmax_map[node.left][1] < node.val
                )
                is_bst_map[node] = is_bst_
                if is_bst_:
                    subtree_size_map[node] = subtree_size_map[node.left] + 1
                    subtree_minmax_map[node] = [subtree_minmax_map[node.left][0], node.val]
                else:
                    subtree_size_map[node] = 0
                    subtree_minmax_map[node] = [node.val, node.val]
                return is_bst_
            if node.right:
                is_bst_ = (
                    node.val < node.right.val
                    and subtree_minmax_map[node.right][0] > node.val
                    and subtree_minmax_map[node.right][1] > node.val
                )
                is_bst_map[node] = is_bst_
                if is_bst_:
                    subtree_size_map[node] = subtree_size_map[node.right] + 1
                    subtree_minmax_map[node] = [node.val, subtree_minmax_map[node.right][1]]
                else:
                    subtree_size_map[node] = 0
                    subtree_minmax_map[node] = [node.val, node.val]
                return is_bst_

            # Has no children
            is_bst_map[node] = True
            subtree_size_map[node] = 1
            subtree_minmax_map[node] = [node.val, node.val]
            return True

        while queue:
            node = queue.pop(0)
            stack.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        while stack:
            node = stack.pop()
            is_bst(node)

        return max([x for x in subtree_size_map.values()])



# The DFS solution is so much simpler (but might not be O(n))
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.max = 0
        r = self.dfs(root)
        return self.max


    def dfs(self, root):
        if root is None:
            return 0, float("inf"), float("-inf")  ####### here we reverse, to make it easy to compare later..
        if root.left == root.right:
            self.max = max(self.max, 1)
            return 1, root.val, root.val

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left[0] == -1 or right[0] == -1:
            return -1, None, None

        # if root.left is not None and root.right is not None:
        if left[2] < root.val < right[1]:
            self.max = max(self.max, left[0] + right[0] + 1)  ########## to get MAx in the middle of Tree, if it is not Pass up, use Global variable !!!!
            return left[0] + right[0] + 1, min(left[1], root.val), max(right[2], root.val)  ########## we must use min and max here!!!!!!!!!!!!
        else:
            return -1, None, None
