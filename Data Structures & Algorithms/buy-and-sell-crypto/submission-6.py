class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minleft = prices[0]
        for num in prices:
            if num - minleft > profit:
                profit = num - minleft
            if minleft > num:
                minleft = num
        return profit