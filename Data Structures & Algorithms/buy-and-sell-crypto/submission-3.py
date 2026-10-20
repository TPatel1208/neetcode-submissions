class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        max_profit = 0
        for p2 in range(1,len(prices)):
            profit = prices[p2] - prices[p1]
            if profit > max_profit:
                max_profit = profit
            elif prices[p2] < prices[p1]:
                p1 = p2
        
        return max_profit
             
            