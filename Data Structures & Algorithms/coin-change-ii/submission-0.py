import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @functools.cache
        def dp(i, j):
            #i index of coins, j remainder amount
            if j == 0:
                return 1
            if j < 0:
                return 0
            if i >= n:
                return 0
            return dp(i+1, j) + dp(i, j - coins[i])
            
        return dp(0, amount)
        