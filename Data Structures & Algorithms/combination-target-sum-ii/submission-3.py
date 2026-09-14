class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        curr = []
        currSum = 0
        res = []
        def backtrack(i):
            nonlocal currSum
            if currSum == target:
                res.append(curr[:])
                return

            if i >= len(candidates):
                return 
            if currSum > target:
                return
            
            
            curr.append(candidates[i])
            currSum += candidates[i]
            backtrack(i+1)
            curr.pop()
            currSum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1)

        backtrack(0)
        return res

        