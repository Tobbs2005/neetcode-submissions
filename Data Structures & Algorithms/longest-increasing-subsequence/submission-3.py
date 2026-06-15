
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        def helper(i, j):
            if i >= n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            take = 0
            skip = helper(i+1, j)
            if j == -1 or nums[i] > nums[j]:
                take = 1 + helper(i+1, i)
            memo[(i,j)] = max(take, skip)
            return max(take, skip)
        return helper(0,-1)
            
            