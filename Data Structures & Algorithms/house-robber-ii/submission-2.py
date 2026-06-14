
class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        dp = {}
        def dfs(i, j):
            if (i >= n) or (i >= j):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
                
            rob = dfs(i+2, j) + nums[i]
            norob = dfs(i+1, j)

            ans = max(rob, norob)
            dp[(i,j)] = ans
            return ans
        
        return max(dfs(0, n-1), dfs(1, n))

