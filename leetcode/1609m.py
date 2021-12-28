# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = [(root, 0)]
        prev_level = 0
        prev_value = None

        while q:
            node, level = q.pop(0)
            assert node

            if level != prev_level:
                prev_value = None
            prev_level = level

            if level % 2 == 0:  # ascending odd numbers
                if node.val % 2 == 0:  # clearly even
                    return False
                if prev_value is not None:
                    if prev_value >= node.val:  # not increasing
                        return False
            else:  # descending even numbers
                if node.val % 2:  # clearly odd
                    return False
                if prev_value is not None:
                    if prev_value <= node.val:  # not decreasing
                        return False
            prev_value = node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return True
