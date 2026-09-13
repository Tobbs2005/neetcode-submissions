class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(0,(0,0))]
        #[cost, (row,col)]
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        seen = set()
        while heap:
            currTime, (row, col) = heapq.heappop(heap)
            if (row,col) in seen:
                continue
            seen.add((row,col))
            res = max(res, grid[row][col])
            if (row, col) == (ROWS-1, COLS-1):
                return res
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                if row+dx < 0 or row+dx >= ROWS or col+dy < 0 or col+dy >= COLS:
                    continue
                newTime = max(grid[row+dx][col+dy], currTime)
                heapq.heappush(heap, (newTime, (row+dx, col+dy)))


        return -1

