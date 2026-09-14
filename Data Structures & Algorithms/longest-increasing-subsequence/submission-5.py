class Solution:
    def lengthOfLIS(self, nums):
        # n = len(nums)
        # memo = [[-1] * (n + 1) for _ in range(n)]

        # def dfs(i, j):
        #     if i == n:
        #         return 0
        #     if memo[i][j + 1] != -1:
        #         return memo[i][j + 1]

        #     LIS = dfs(i + 1, j)

        #     if j == -1 or nums[j] < nums[i]:
        #         LIS = max(LIS, 1 + dfs(i + 1, i))

        #     memo[i][j + 1] = LIS
        #     return LIS

        # return dfs(0, -1)



        #build into bottom up
        # fill from bottom right
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n+1)]
        for j in range(n+1):
            dp[n][j] = 0
        for row in range(n-1, -1, -1):
            for col in range(n-1, -2, -1):
                LIS = dp[row + 1][col+1]

                if col == -1 or nums[col] < nums[row]:
                    LIS = max(LIS, 1 + dp[row + 1][row+1])
                dp[row][col+1] = LIS
        return dp[0][0]
