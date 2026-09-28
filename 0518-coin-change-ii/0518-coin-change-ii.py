class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        def f(i,t):
            if t==0:
                return 1
            elif i<0:
                return 0
            if dp[i][t]!=-1:
                return dp[i][t]
            pick,skip=0,0
            if t>=coins[i]:
                pick=f(i,t-coins[i])
            skip=f(i-1,t)
            dp[i][t]=pick+skip
            return dp[i][t]
        return f(len(coins)-1,amount)
        