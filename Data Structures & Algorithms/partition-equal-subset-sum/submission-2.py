class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        goal = total // 2

        n = len(nums)
        dp = [[False] * (goal + 1) for _ in range(n + 1)]
        dp[n][0] = True

        # dp[row][col] = dp[row+1][col-dp[row]] and dp[row+1][col]
        for col in range(goal + 1):
            for row in range(n - 1, -1, -1):   # start one above the base row, go up to 0
             
                dp[row][col] = dp[row+1][col] 
                if col >= nums[row]:
                    dp[row][col] = dp[row][col] or dp[row+1][col-nums[row]] 
        return dp[0][goal]

