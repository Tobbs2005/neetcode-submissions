class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] pre = new int[n];
        int[] post = new int[n];
        int max = 0;
        int max2 = 0;
        for(int i = 0; i < n; i++) {
            max = Math.max(max, height[i]);
            pre[i] = Math.max(max, height[i]);
            max2 = Math.max(max2, height[n-i-1]);
            post[n-i-1] = Math.max(max2, height[n-i-1]);
        }


        //build output
        int res = 0;
        for(int i = 0; i < n; i++){
            int curr = Math.min(pre[i], post[i]) - height[i];
            res += curr;
        }
        return res;
    }
}
