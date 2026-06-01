class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0
            
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0

            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
        
        
        for i in range(ROWS):
            for j in range(COLS):
                ans = max(ans, dfs(i, j))
        return ans
        