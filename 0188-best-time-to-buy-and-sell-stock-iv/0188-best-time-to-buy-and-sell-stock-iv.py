class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n=len(prices)
        dp=[[[-1]*k for _ in range(2)] for _ in range(n)]
        def f(i,flag,ct):
            if i==n or ct==k:
                return 0
            if dp[i][flag][ct]!=-1:
                return dp[i][flag][ct]
            skip=f(i+1,flag,ct)
            if flag==True:
                buy=-prices[i]+f(i+1,False,ct)
                ans=max(buy,skip)
            else:
                sell=prices[i]+f(i+1,True,ct+1)
                ans=max(sell,skip)
            dp[i][flag][ct]=ans
            return ans
        return f(0,True,0)



        


        