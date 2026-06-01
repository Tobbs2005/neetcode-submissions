class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        n = len(board)
        m = len(board[0])
        length = len(word)
        visited = set()
        def backtrack(curr, x, y):
            if curr == length:
                return True
            for a, b in directions:
                nx = a+x
                ny = b+y
                if nx >= m or nx < 0 or ny>= n or ny <0:
                    continue
                if (nx,ny) in visited:
                    continue
                
                if board[ny][nx] == word[curr]:
                    visited.add((nx,ny))
                    ans = backtrack(curr+1, nx, ny)
                    visited.remove((nx,ny))
                    if ans:
                        return True
            return False

       
        ans = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((j, i))
                    ans = ans or backtrack(1, j, i)
                    visited.remove((j,i))
        return ans
        
        
        

            

