class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # if len(coins)==1 and coins[0]<amount:
        #     return -1
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n+1)]
        def f(i,t):
        
            if t==0:
                return 0
            if t<0:
                return float("inf")
            if i>=n:
                return float('inf')
            if dp[i][t]!=-1:
                return dp[i][t]
            
            
            pick=1+f(i,t-coins[i])
            skip=f(i+1,t)
            ans=min(pick,skip)
            dp[i][t]=ans
            return ans
        flag=f(0,amount)
        if flag==float('inf'):
            return -1
        else:
            return flag
        



        