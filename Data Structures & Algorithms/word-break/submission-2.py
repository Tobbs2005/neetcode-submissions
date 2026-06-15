class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        memo = {}
        def dp(start):
            if start >= n:
                return True
            if (start) in memo:
                return memo[(start)]
            for end in range(start, n):
                word = s[start:end+1]
                if word in words:
                    if dp(end+1):
                        memo[(start)] = True
                        return True
       
            memo[(start)] = False
            return False
        return dp(0)
        

        
                
