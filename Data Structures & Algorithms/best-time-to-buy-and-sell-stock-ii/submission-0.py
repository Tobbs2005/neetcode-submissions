class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers
        #i is bought index
        #j increments every round
        #if decreasing next round, sell this round, i = j + 1
        n = len(prices)
        i = 0
        j = 0
        profit = 0
        while j < n:
            if j == n-1:
                profit = profit + prices[j] - prices[i]
                break
            if prices[j] > prices[j+1]:
                profit = profit + prices[j] - prices[i]
                i = j+1
            j += 1


        return profit