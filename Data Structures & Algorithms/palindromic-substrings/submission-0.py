import functools
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        @functools.cache
        def isPali(i, j):
            if s[i] == s[j] and (j-i+1 <= 3 or isPali(i+1, j-1)):
                return True
            return False
        
        count = 0
        for start in range(n):
            for end in range(start, n):
                if isPali(start, end):
                    count += 1
        return count
