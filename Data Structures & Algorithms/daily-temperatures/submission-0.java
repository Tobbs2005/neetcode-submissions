class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<int[]>();
        //monotonic decreasing [temp][index]
        int[] ans = new int[temperatures.length];
        int i = 0;
        while(i<temperatures.length){
            while(!stack.isEmpty() && stack.peek()[0] < temperatures[i]){
                //calculate val
                int[] curr = stack.pop();
                ans[curr[1]] = i - curr[1];
            }
            stack.push(new int[]{temperatures[i], i});
            i++;
        }
        return ans;
        


    }
}
