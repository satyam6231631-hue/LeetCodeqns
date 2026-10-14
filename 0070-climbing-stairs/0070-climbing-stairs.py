class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(i):
           
            if i==1:
                return 1
            if i==2:
                return 2
            
            if dp[i]!=-1:
                return dp[i]
            one=f(i-1)
            two=f(i-2)
            ans=one+two
            dp[i]=ans
            return ans
        return f(n)

        