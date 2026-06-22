class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0])

        ROWS = len(matrix)
        COLS = len(matrix[0])
        while left < right:
            mid = (left+right) // 2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] == target:
                return True
            if matrix[row][col] >= target:
                right = mid
            else:
                left = mid + 1
        return False