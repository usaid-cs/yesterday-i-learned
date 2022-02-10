import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    List<Integer> dfs(TreeNode node, List<Integer> result) {
        if (result == null) {
            result = new ArrayList<Integer>();
        }
        if (node == null) {
            return result;
        }
        dfs(node.left, result);
        result.add(node.val);
        dfs(node.right, result);
        return result;
    }

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> list1 = dfs(root1, null);
        List<Integer> list2 = dfs(root2, null);
        List<Integer> list3 = new ArrayList<Integer>();

        while (!(list1.isEmpty() && list2.isEmpty())) {
            if (!(list1.isEmpty() || list2.isEmpty())) {
                if (list1.get(0) < list2.get(0)) {
                    list3.add(list1.remove(0));
                } else {
                    list3.add(list2.remove(0));
                }
            } else if (list1.isEmpty()) {
                list3.add(list2.remove(0));
            } else if (list2.isEmpty()) {
                list3.add(list1.remove(0));
            }
        }
        return list3;
    }
}
