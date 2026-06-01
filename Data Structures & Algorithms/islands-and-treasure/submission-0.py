class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        

        while queue:
            curr = queue.popleft()
            r, c, depth = curr
            for x, y in ((1,0),(0,1),(-1,0), (0,-1)):
                nr = r + x
                nc = c + y
                
                if nc < 0 or nc >= COLS:
                    continue
                if nr < 0 or nr >= ROWS:
                    continue
                if grid[nr][nc] == -1 or grid[nr][nc] == 0:
                    continue
                if grid[nr][nc] == 2147483647:
                    
     
                    grid[nr][nc] = depth + 1
                    queue.append((nr, nc, depth+1))


                


        