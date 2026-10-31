class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        def f(i):
            if i==n:
                return 0
            if i==n-1:
                return cost[n-1]
            if dp[i]!=-1:
                return dp[i]
            one=cost[i]+f(i+1)
            two=cost[i]+f(i+2)
            dp[i]=min(one,two)
            return dp[i]
        return min(f(0),f(1))
            



        