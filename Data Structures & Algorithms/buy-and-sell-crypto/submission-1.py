class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for day, price in enumerate(prices[1:]):
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit



        