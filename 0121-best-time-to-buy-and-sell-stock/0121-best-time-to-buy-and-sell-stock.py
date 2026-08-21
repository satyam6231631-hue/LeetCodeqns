class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,buy=0,prices[0]
        for i in range(len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            else:
                profit=max(prices[i]-buy,profit)
        return profit
        