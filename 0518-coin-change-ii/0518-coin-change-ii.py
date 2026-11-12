class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        dp[0][0]=1
        for t in range(1,amount+1):
            if t%coins[0]==0:
                dp[0][t]=1
            else:
                dp[0][t]=0
        
        for i in range(1,n):
            for t in range(amount+1):
                dp[i][t]+=dp[i-1][t]
                if t>=coins[i]:
                    dp[i][t]+=dp[i][t-coins[i]]
        return dp[n-1][amount]
        