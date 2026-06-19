import functools
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @functools.cache
        def dp(i, j):
            print(j)
            #i index, j curr sum
            if i >= n:
                if j == 0:
                    return 1
                return 0
            return dp(i+1, j+nums[i]) + dp(i+1, j-nums[i])
        return dp(0, target)
            