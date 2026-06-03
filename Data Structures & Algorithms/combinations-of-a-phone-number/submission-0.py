class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        curr = []
        n = len(digits)
        def dfs(i):
            if i >= n:
                res.append("".join(curr))
                return
            
            digit = digits[i]
            letters = digitToChar[digit]
            for letter in letters:
                curr.append(letter)
                dfs(i+1)
                curr.pop()
        dfs(0)
        return res
