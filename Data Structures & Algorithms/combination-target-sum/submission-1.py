class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        ans = []
        curr = []
        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                ans.append(curr.copy())
                return
            if(curr_sum > target or i >= len(nums)):
                return
            
            # two descisions 
            #include
            curr.append(nums[i])
            dfs(i, curr, curr_sum+nums[i])
            curr.pop()

            #exclude
            dfs(i+1, curr, curr_sum)
        dfs(0, [], 0)
        return ans
