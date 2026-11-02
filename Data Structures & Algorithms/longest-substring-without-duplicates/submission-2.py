class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        fs = set()
        n = len(s)
        res = 0
        for r in range(n):

            while s[r] in fs:
                fs.remove(s[l])
                l += 1
                
            fs.add(s[r])
            res = max(res, r-l+1)

        return res

   