class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int num : nums){
            set.add(num);
        }
        int res = 0;
        for(int i : set) {
            int length = 0;
            int curr = i;
            while(set.contains(curr++)) {
                length++;
                
            }
            res = Math.max(res, length);
        }
        return res;
    }
}
