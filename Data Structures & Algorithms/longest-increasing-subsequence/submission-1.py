import functools
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        @functools.cache
        def helper(i, j):
            if i >= n:
                return 0
            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + helper(i+1, i)
            skip = helper(i+1, j)
            return max(take, skip)
        return helper(0,-1)
            
            