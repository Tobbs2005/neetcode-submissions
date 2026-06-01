class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, w):
        node = self
        for c in w:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(node, word, row, col):
            if row < 0 or row >= rows or col<0 or col >= cols or board[row][col] not in node.children or (row,col) in visited:
                return
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.end:
                res.add(word)

            dfs(node, word, row+1,col)
            dfs(node, word, row-1,col)
            dfs(node, word, row,col+1)
            dfs(node, word, row,col-1)
            
            visited.remove((row,col))




        for r in range(rows):
            for c in range(cols):
                dfs(root,"", r, c)
        return list(res)


