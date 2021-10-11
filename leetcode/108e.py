# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        arr = nums
        if not arr:
            return None

        def recurse(sub_arr):
            if not sub_arr:
                return None
            middle = len(sub_arr) // 2
            node = TreeNode(sub_arr[middle])
            node.left = recurse(sub_arr[:middle])
            node.right = recurse(sub_arr[middle + 1:])
            return node

        return recurse(arr)
