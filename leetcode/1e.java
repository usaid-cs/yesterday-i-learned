import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            map.put(num, i);
        }

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (map.containsKey(target - num)) {
                if (map.get(target - num) != i) {
                    return new int[] {i, map.get(target - num)};
                }
            }
        }

        return new int[] {};
    }
}
