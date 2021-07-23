class TreeNode:
    val = None
    left = None
    right = None


class Solution:
    def isValidBST(self, root, lowest=None, highest=None) -> bool:
        ohno()
        if not root:
            return True
        if root.left:
            if root.left.val >= root.val:
                return False
            if lowest is None:
                lowest = root.val
            if root.left.val >= lowest:
                return False
            lowest = min(root.left.val, lowest)
        if root.right:
            if root.right.val <= root.val:
                return False
            if highest is None:
                highest = root.val

            if root.right.val <= highest:
                return False
            highest = max(root.right.val, highest)
        return self.isValidBST(root.left, lowest, highest) and \
            self.isValidBST(root.right, lowest, highest)
