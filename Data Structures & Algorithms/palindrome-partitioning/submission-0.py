class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []
        n = len(s)
        def isP(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        def backtrack(i):
            if i>=n:
                ans.append(curr.copy())
                return
            for j in range(i, n):
                if isP(i,j):
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
        backtrack(0)
        return ans

            