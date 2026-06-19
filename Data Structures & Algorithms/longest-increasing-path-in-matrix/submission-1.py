import functools
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        @functools.cache
        def dfs(i,j):
            # returns longest increasing path from row i col j
            longest = 1
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx = i+dx
                ny = j+dy
                if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS:
                    continue
                
                if matrix[i][j] < matrix[nx][ny]:
                    longest = max(longest, 1 + dfs(nx, ny))
            return longest

        ans = 1
        for i in range(ROWS):
            for j in range(COLS):
                ans = max(ans, dfs(i,j))
        return ans