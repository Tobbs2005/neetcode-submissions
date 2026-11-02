from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        n = len(s)
        res = 0
        resLen = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j or j-i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]== s[j]
                if dp[i][j]:
                    if j-i+1 > resLen:
                        res = i
                        resLen = j-i+1
            

        return s[res: res+resLen]
        


