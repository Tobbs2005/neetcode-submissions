class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(row,col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for i in range(COLS):
            for j in range(ROWS):
                if grid[j][i] == "1":
                    ans += 1
                    dfs(j,i)
        return ans