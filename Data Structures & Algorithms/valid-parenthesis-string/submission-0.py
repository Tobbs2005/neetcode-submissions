class Solution:
    def checkValidString(self, s: str) -> bool:
        minL = 0
        maxL = 0
        for c in s:
            if c == '(':
                minL += 1
                maxL += 1
            elif c == ')':
                minL -= 1
                maxL -= 1
            else:
                maxL += 1
                minL -= 1
            if maxL < 0:
                return False
            if minL < 0:
                minL = 0
        return minL == 0