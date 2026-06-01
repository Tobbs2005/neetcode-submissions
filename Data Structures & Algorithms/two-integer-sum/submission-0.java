class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> comp = new HashMap<Integer, Integer>();
        // comp , index
        for(int i = 0; i < nums.length; i ++){
            int curr = target - nums[i];
            if(comp.containsKey(curr)){
                return new int[] {comp.get(curr), i};
            }

            comp.put(nums[i], i);
        }
        return new int[]{};
    }
}
