class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - ord("a")
            if not node.children[i]:
                node.children[i] = Node()
            node = node.children[i]
        node.is_end = True



    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            i = ord(c) - ord("a")
            if node.children[i]:
                node = node.children[i]
            else:
                return False
        return node.is_end


        
        # def dfs(node, remain):
        #     if remain == "":
        #         return node.is_end
        #     c = remain[0]
        #     i = ord(c) - ord('a')
        #     if node.children[i] is None:
        #         return False
        #     return dfs(node.children[i], remain[1:])
        
        # return dfs(self.root, word)

        

    def startsWith(self, prefix: str) -> bool:
        def dfs(node, remain):
            if remain == "":
                return True
            c = remain[0]
            i = ord(c) - ord('a')
            if node.children[i] is None:
                return False
            return dfs(node.children[i], remain[1:])
        
        return dfs(self.root, prefix)
        
        