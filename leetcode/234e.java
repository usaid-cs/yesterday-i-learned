/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> lst = new ArrayList<>();
        ListNode cur = head;

        while (cur != null) {
            lst.add(cur.val);
            cur = cur.next;
        }

        // List<Integer> lst2 = lst.subList(0, lst.size());
        List<Integer> lst2 = new ArrayList(lst);
        Collections.reverse(lst2);
        // System.out.println(lst2);
        return lst.equals(lst2);
    }
}
