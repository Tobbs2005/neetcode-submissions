import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = float('inf')
        @functools.cache
        def dp(curr, count):
    
            if curr  == 0:
                nonlocal ans
                ans = min(ans, count)
                return
            if curr < 0:
                return
            for coin in coins:
                dp(curr-coin, count + 1)

        dp(amount, 0)
        if ans == float('inf'):
            return -1
        return ans

