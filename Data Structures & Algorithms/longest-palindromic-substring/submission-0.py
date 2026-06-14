class Solution:
    def longestPalindrome(self, s: str) -> str:
            resStart, resEnd = 0,0
            n = len(s)
            dp = [[False]*n for _ in range(n)]

            for end in range(0, n):
                for start in range(0, end+1):
                    if s[start] == s[end] and (end-start <= 2 or dp[start+1][end-1]):
                        dp[start][end] = True
                        if (resEnd-resStart+1) < (end-start+1):
                            resStart = start
                            resEnd = end
            return s[resStart:resEnd+1]
                        
