import functools
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @functools.cache
        def dp(i,j):
            #j 0 not cooldown, 1 cooldown, 2 holding
            if i == 0:
                if j == 0: return 0
                if j == 2: return -prices[0]
                if j == 1: return float('-inf')
            
            if j == 0:
                return max(dp(i-1, 0), dp(i-1, 1))
            if j == 1:
                return dp(i-1, 2)+prices[i]
            if j == 2:
                return max(dp(i-1, 2), dp(i-1, 0)-prices[i])
        return max(dp(n-1, 0), dp(n-1, 1))  # best outcome on last day, not holding

                            
                        