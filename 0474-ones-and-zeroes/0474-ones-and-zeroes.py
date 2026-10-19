class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[[-1] * (n+1) for _ in range(m+1)] for _ in range(len(strs))]
       
        def f(i,zero,one):
            if zero> m or one>n:
                return float("-inf")
            if i==len(strs):
                return 0
            if dp[i][zero][one]!=-1:
                return dp[i][zero][one]
            z=0
            o=0
            for j in strs[i]:
                if j=="1":
                    o+=1
                else:
                    z+=1
            pick=1+f(i+1,zero+z,one+o)
            
            skip=f(i+1,zero,one)
            ans=max(pick,skip)
            dp[i][zero][one]=ans
            return ans
        return f(0,0,0)


            




        