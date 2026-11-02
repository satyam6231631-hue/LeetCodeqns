class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        dp=[-1]*(n+1)
        def f(i,end):
            if i<end:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick,skip=0,0
            pick=nums[i]+f(i-2,end)
            skip=f(i-1,end)
            dp[i]=max(pick,skip)
            return dp[i]
        case1=f(n-1,1)
        dp=[-1]*(n+1)
        case2=f(n-2,0)
        return max(case1,case2)

        