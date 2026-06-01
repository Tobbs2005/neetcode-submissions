class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(curr : str, l:int, r:int):
            if(len(curr) == 2*n and l == r):
                ans.append(curr)
                return
            if(l<n):
                curr += '('
                helper(curr, l+1, r)
                curr = curr[:len(curr)-1]
            if(r<l):
                curr += ')'
                helper(curr, l, r+1)
                curr = curr[:len(curr)-1]
                
            return
        helper("", 0, 0)
        return ans
            
        