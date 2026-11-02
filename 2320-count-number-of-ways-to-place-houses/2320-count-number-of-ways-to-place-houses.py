class Solution:
    def countHousePlacements(self, n: int) -> int:
        md=10**9 +7
        dp=[-1]*(n+1)
        def f(i):
            if i==1:
                return 2
            if i==0:
                return 1
            if dp[i]!=-1:
                return dp[i]

           
            place=f(i-2)
            skip=f(i-1)
            dp[i]=place+skip
            return dp[i]
        ans=f(n)
        return (ans*ans)%md

        


        