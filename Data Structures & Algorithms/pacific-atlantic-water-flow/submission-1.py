class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        queue = deque()
       


        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        def bfs(queue, ocean):
            q = deque(queue)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = dr + r
                    nc = dc + c
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if ocean[nr][nc]:
                        continue
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    q.append((nr,nc))
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res

    



