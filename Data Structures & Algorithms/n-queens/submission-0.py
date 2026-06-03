class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        negdiag = set()
        res = []
        curr = [["."] * n for _ in range(n)]
        def backtrack(row):
            if row >= n:
                res.append(["".join(row) for row in curr])
                return
            for c in range(n):
                if (c in col) or (row-c in negdiag) or (row+c in diag):
                    continue
                col.add(c)
                diag.add(row+c)
                negdiag.add(row-c)
                curr[row][c] = "Q"

                backtrack(row+1)
                
                col.remove(c)
                diag.remove(row+c)
                negdiag.remove(row-c)
                curr[row][c] = "."
        backtrack(0)
        return res
