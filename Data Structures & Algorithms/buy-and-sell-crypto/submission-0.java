class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 0;
        int res = 0;
        while(right<prices.length){
            int curr = prices[right] - prices[left];
            res = Math.max(res, curr);
            if(curr <= 0){
                left=right;
            }
            right++;
        }
        return res;
    }
}
