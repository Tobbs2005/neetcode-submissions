class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def backtrack(i, numOpen):
            if i == n*2:
                res.append("".join(curr))
                return
            left = n*2 - i
            
            if left > numOpen:
                curr.append("(")
                backtrack(i+1, numOpen+1)
                curr.pop()
            if numOpen > 0:
                curr.append(")")
                backtrack(i+1, numOpen-1)
                curr.pop()
        backtrack(0, 0)
        return res


