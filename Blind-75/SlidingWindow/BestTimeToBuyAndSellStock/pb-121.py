from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1 
        maxP = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]: # profitable
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else: # not profitable
                buy = sell
            sell += 1
        return maxP