class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        n = len(word1)
        m = len(word2)

        res = []

        while p1 < n and p2 < m:
            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1

        if p1 == n:
            while p2 < m:
                res.append(word2[p2])
                p2 += 1
        else:
            while p1 < n:
                res.append(word1[p1])
                p1 += 1
        return "".join(res)


        