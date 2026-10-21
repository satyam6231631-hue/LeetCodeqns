class Solution:
    def numDecodings(self, s: str) -> int:
        
        n=len(s)
        dp=[0]*(n+1)

        def f(i):
            
            if i>=n:
                return 1
            if s[i]=='0':
                return 0
            if dp[i]!=0:
                return dp[i]
            one,two=0,0
            if 1<=int(s[i:i+1])<=9:
                one=f(i+1)
            if 10<=int(s[i:i+2])<=26:
                two=f(i+2)
            dp[i]=one+two
            return dp[i]
        return f(0)
            

        

        


