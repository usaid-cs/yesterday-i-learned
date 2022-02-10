class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int middle = -1;
        int num;

        while (left <= right) {
            middle = (left + right) / 2;
            num = nums[middle];
            if (num == target) {
                return middle;
            }
            if (num < target) {
                left = middle + 1;
            } else if (num > target) {
                right = middle - 1;
            }
        }
        return -1;
    }
}
