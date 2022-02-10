class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int head = 0;
        int removed = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[head]) {
                head++;
                removed++;
                nums[head] = nums[i];
            }
        }
        return removed + 1;
    }
}
