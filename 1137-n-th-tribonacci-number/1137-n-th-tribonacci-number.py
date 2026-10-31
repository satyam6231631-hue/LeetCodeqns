class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(i):
            if i<=1:
                return i
            if i==2:
                return 1
            if dp[i]!=-1:
                return dp[i]
            dp[i]=f(i-1)+f(i-2)+f(i-3)
            return dp[i]
        return f(n)
        