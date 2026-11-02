from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[n][m] = True

        for i in range(n,-1,-1):
            for j in range(m-1,-1,-1):
                match = (i < n and (s[i] == p[j] or p[j] == '.'))
                if j < m-1 and p[j+1] == '*':
                    # not take or take
                    take = False
                    if match:
                        take = dp[i+1][j]
                    res = dp[i][j+2] or take
                else:
                    res = match and dp[i+1][j+1]
                dp[i][j] = res
        return dp[0][0]



        # @cache
        # def dp(i, j):
        #     if i >= n and j >= m:
        #         return True
        #     elif j>= m:
        #         return False
        #     match = (i < n and( s[i] == p[j] or p[j] == '.'))
        #     if j < m-1 and p[j+1] == '*':
        #         # not take or take
        #         take = False
        #         if match:
        #             take = dp(i+1, j)
        #         res = dp(i, j+2) or take
        #     else:
        #         res = match and dp(i+1, j+1)
        #     return res
        # return dp(0,0)




