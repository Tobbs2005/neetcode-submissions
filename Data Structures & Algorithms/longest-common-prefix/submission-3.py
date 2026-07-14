class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        curr = 0
        minlength = min(len(s) for s in strs)
        print(minlength)

        while True:
            
            if curr == minlength:
                break
            for i in range(len(strs) - 1):
                if strs[i][curr] == strs[i+1][curr]:
                    continue
                   
                else:
                    return ans
            ans += strs[0][curr]
            curr += 1
        return ans


        