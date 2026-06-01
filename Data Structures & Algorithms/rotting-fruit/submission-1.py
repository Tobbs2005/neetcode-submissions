class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        def getNeighbours(row, col):
            neighbours = []
            if(row+1 < rowSize and grid[row+1][col] == 1):
                neighbours.append([row+1, col])

            if(row-1 >= 0 and grid[row-1][col] == 1):
                neighbours.append([row-1, col])

            if(col+1 < colSize and grid[row][col+1] == 1):
                neighbours.append([row, col+1])

            if(col-1 >= 0 and grid[row][col-1] == 1):
                neighbours.append([row, col-1])

            return neighbours


        rowSize = len(grid)
        colSize = len(grid[0])

        queue = deque()
        fresh = 0
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        time = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                currRow = curr[0]
                currCol = curr[1]
                neighbours = getNeighbours(currRow, currCol)
                for neighbour in neighbours:
                    queue.append(neighbour)
                    grid[neighbour[0]][neighbour[1]] = 2
                    fresh -= 1
            time += 1

        if fresh > 0: 
            return -1
        return time -1
        





        

            

        