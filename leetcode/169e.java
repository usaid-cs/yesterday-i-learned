class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> foo = new HashMap<>();

        if (nums.length <= 0) {
            return 0;
        }

        for (int num : nums) {
            if (foo.containsKey(num)) {
                foo.put(num, foo.get(num) + 1);
            } else {
                foo.put(num, 1);
            }
        }

        int maxKey = -1;
        int maxCount = 0;
        for (int key : foo.keySet()) {
            int count = foo.get(key);
            if (count > maxCount) {
                maxKey = key;
                maxCount = count;
            }
        }

        return maxKey;
    }
}
