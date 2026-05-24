class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for day, price in enumerate(prices):
            if day == 0:
                continue
            buy = min(prices[:day])
            profit = max(profit, price - buy)
        return profit



        