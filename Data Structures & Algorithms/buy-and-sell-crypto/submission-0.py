class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        p1 = 0
        for p2 in range(1,len(prices)):
            if (prices[p2] - prices[p1]) > max_profit:
                max_profit = prices[p2] - prices[p1]
                p2+=1
            elif(prices[p2]<prices[p1]):
                p1 = p2
                p2 +=1
            else:
                p2+=1
        return max_profit