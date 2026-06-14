import functools
class Solution:

    def rob(self, nums: List[int]) -> int:
        # top down
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        @functools.cache
        def dfs(i, j):
            if (i >= n) or (i >= j):
                return 0
                
            rob = dfs(i+2, j) + nums[i]
            norob = dfs(i+1, j)

            return max(rob, norob)
        
        return max(dfs(0, n-1), dfs(1, n))

