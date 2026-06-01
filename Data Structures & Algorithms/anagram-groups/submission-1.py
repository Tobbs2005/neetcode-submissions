class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            word = [0] * 26
            for c in string:
                word[ord('a')-ord(c)] += 1
            #add to hash
            ans[tuple(word)].append(string)
        res = []
        for value in ans.values():
            res.append(value)
        return res