class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):

            grid[row][col] = "0"

            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                nx = dx + row
                ny = dy + col
                if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS:
                    continue
                if grid[nx][ny] == "0":
                    continue
                dfs(nx, ny)
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
                    
        return res