class Solution:
    def minWindow(self, s: str, t: str) -> str:


        window = defaultdict(int)
        need = defaultdict(int)

        for c in t:
            need[c] += 1
        
        r = 0
        l = 0

        counter = len(need) # how many letters we need

        n = len(s)
        ans = ""
        length = float("inf")
        while r < n:
            window[s[r]] += 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                counter -= 1
            
            while counter <= 0:
                # we have all letters
                if r-l + 1< length:
                    length = r-l + 1
                    ans = s[l:r+1]
                if s[l] in need and window[s[l]] == need[s[l]]:
                    counter += 1

                window[s[l]] -= 1
                
                l += 1
            r += 1
        return ans



