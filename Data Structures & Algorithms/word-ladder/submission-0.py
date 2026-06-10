class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set()
        for word in wordList:
            wordset.add(word)
        
        q = deque()

        alphabets = ['a','b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','r','q','s','t','u','v','w','x','y','z']

        q.append((beginWord, 1))

        seen = set()
        while q:
            print(q)
            curr = q.popleft()
            word = list(curr[0])
            count = curr[1]

            if curr[0] == endWord:
                return count


            for i in range(len(word)):
                for a in alphabets:
                    new = word.copy()
                    new[i] = a
                    new_word = "".join(new)
                    if new_word in seen:
                        continue
                    if new_word not in wordset:
                        continue
                    seen.add(new_word)
                    q.append((new_word, count+1))


        return 0



