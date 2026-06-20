import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # at each character, skip if curr matches
        # three choices

        # our base case if word1 == word2 return 0

        n = len(word1)
        m = len(word2)
        @functools.cache
        def dp(i,j):
            if i >= n:
                return m-j
            if j >= m:
                return n-i

            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            
            #1 insert
            res = min(dp(i + 1, j), dp(i, j + 1))
            res = min(res, dp(i + 1, j + 1))
            return res + 1
        
        return dp(0,0)