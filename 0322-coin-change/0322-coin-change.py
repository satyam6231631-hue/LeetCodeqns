class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        if amount==0:
            return 0
        
            
        dp=[[float("inf")]*(amount +1) for _ in range(n)]
        dp[0][0]=0
        for t in range(1,amount+1):
            if t%coins[0]==0:
                dp[0][t]=t//coins[0]
            else:
                dp[0][t]=float("inf")
        for i in range(1,n):
            for t in range(amount+1):
                dp[i][t]=min(dp[i][t],dp[i-1][t])
                if t>=coins[i]:
                    dp[i][t]=min(dp[i][t],1+dp[i][t-coins[i]])
        if dp[n-1][amount]==float("inf"):
            return -1

        return dp[n-1][amount]

                
                




        