class Solution {
    public int maxSubArray(int[] nums) {
        if (nums.length < 1) {
            return 0;
        }

        Integer[] maxSums = new Integer[nums.length];
        maxSums[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            maxSums[i] = Math.max(maxSums[i - 1] , 0) + nums[i];
        }

        List<Integer> maxSumsList = Arrays.asList(maxSums);
        Collections.sort(maxSumsList);

        return maxSumsList.get(maxSumsList.size() - 1);
    }
}
