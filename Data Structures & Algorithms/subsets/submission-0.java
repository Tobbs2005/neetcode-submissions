class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        List<Integer> subset = new ArrayList<>();

        recursion(nums, ans, subset, 0);
        return ans;

    }
    public void recursion(int[] nums, List<List<Integer>> ans, List<Integer> curr, int index){
        if(index >= nums.length){
            ans.add(new ArrayList<>(curr));
            return;
        }
        curr.add(nums[index]);
        recursion(nums, ans, curr, index + 1);
        curr.remove(curr.size() - 1);
        recursion(nums, ans, curr, index + 1);

        

    }
}
