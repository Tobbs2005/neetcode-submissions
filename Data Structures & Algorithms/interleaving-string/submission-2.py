import functools
class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n = len(s1)
        m = len(s2)
        if n+m != len(s3):
            return False

        @functools.cache
        def dp(i,j):
            if i+j == len(s3):
                return True
            if i >= n:
                return True if s3[i+j:] == s2[j:] else False
            if j >= m:
                return True if s3[i+j:] == s1[i:] else False
            if s1[i] == s3[i+j]:
                if dp(i+1, j):
                    return True
            if s2[j] == s3[i+j]:
                if dp(i, j+1):
                    return True
            return False
            
        return dp(0,0)