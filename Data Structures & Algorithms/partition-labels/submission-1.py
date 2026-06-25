class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        curr = 0
        currLast = 0
        for i, c in enumerate(s):
            currLast = max(currLast, lastIndex[c])
            curr += 1
            if i == currLast:
                res.append(curr)
                curr = 0
        return res