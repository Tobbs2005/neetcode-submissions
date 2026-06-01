class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - ord("a")
            if not node.children[i]:
                node.children[i] = Node()
            node = node.children[i]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, curr):
            if curr == len(word):
                return node.is_end

            c = word[curr]
            i = ord(c)-ord("a")
            ans = False
            #case equals .
            if c == ".":
                #not sure if this works
                for child in node.children:
                    if not child:
                        continue
                    ans = ans or dfs(child, curr+1)
                return ans

            # case one child
            if not node.children[i]:
                return False
            return dfs(node.children[i], curr+1)
        return dfs(self.root, 0)

        
