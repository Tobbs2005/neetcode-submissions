class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, our min cost is the min of i-1 and i-2 steps

        #cost to step
        n = len(cost)
        ctp = [0]*(n)

   
        ctp[0] = cost[0]
        ctp[1] = cost[1]

        for i in range(2, n):
            ctp[i] = min(ctp[i-1], ctp[i-2]) + cost[i]
        print(ctp)
        return min(ctp[n-1], ctp[n-2])
        