import functools
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        @functools.cache
        def dfs(i, j):
            ans = 0
            if i >= n or j >= m:
                return 0
            if text1[i] == text2[j]:
                ans = 1 + dfs(i+1, j+1)
            else:
                ans = max(dfs(i+1, j+1), dfs(i, j+1), dfs(i+1, j))
            return ans
        return dfs(0,0)
            