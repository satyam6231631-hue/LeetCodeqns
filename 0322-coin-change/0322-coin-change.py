class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
       
        def f(i,t):
            if t<0:
                return float('inf')
            elif t==0:
                return 0
            if i==len(coins):
                return float('inf')
            if dp[i][t]!=-1:
                return dp[i][t]
            pick=1+f(i,t-coins[i])
            skip=f(i+1,t)
            ans=min(pick,skip)
            dp[i][t]=ans
            return ans
        ans=f(0,amount)
        if ans==float('inf'):
            return -1
        else:
            return ans
            
        
            