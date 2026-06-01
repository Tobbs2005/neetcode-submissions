class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] pre = new int[length];
        int[] post = new int[length];
        pre[0] = nums[0];
        post[length-1] = nums[length-1];
        for(int i = 1; i < length; i++) {
            pre[i] = pre[i-1] * nums[i];
            post[length-i-1] = post[length-i] * nums[length-i-1];
        }
        int[] res = new int[length];
        res[0] = post[1];
        res[length-1] = pre[length-2];
        for(int i = 1; i < length-1; i++){
            res[i] = pre[i-1]* post[i+1];
        }
        return res;
    }
}  
