class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(row, col):
            if  row >= n or row < 0 or col >= m or col < 0 or board[row][col] == "S" or board[row][col] == "X":
                return
            board[row][col] = "S"

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        for i in range(m):
            dfs(0, i)
            dfs(n-1, i)
                
        for row in range(n):
            for col in range(m):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
