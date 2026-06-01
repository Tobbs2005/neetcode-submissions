class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        i = 0
        candidates.sort()
        ans = []
        curr = []
        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                ans.append(curr.copy())
                return
            if(curr_sum > target or i >= len(candidates)):
                return
            curr.append(candidates[i])
            dfs(i+1, curr, curr_sum + candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, curr_sum)
            
        dfs(0, [], 0)
        return ans
