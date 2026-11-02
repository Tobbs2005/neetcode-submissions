from functools import cache
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        @cache
        def dp(i):
            if i >= n-1:
                return 1 
            temp = 1
            for curr in range(i+1, n):
                if nums[curr] > nums[i]:
                    temp = max(temp, dp(curr) + 1)

            return temp
        res = 0
        for i in range(n):
            res = max(res, dp(i))
        return res
