class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        # n rows, m cols

        # base cases where j == m
        # dp[i][j] = 1
        # for all i, loop dp[i][m] = 1

        # if letter equal: take or not take
        # dp[i][j] = dp[i+1][j+1] + dp[i+1][j]

        # if not equals
        #dp[i][j] = dp[i+1][j]
        

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][m] = 1
        
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if t[col] == s[row]:
                    dp[row][col] = dp[row+1][col+1] + dp[row+1][col]
                else:
                    dp[row][col] = dp[row+1][col]
        return dp[0][0]
