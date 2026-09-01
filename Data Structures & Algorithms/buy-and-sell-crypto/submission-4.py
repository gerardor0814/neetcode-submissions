class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            temp = 0
            if prices[l] < prices[r]:
                temp = prices[r] - prices[l]
                profit = max(profit, temp)
            else:
                l = r
            r += 1
        return profit 