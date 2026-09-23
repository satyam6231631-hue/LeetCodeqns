class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1]*len(nums)
        def f(i):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            if dp[i]!=-1:
                return dp[i]
            pick=nums[i]+f(i-2)
            skip=f(i-1)
            ans=max(pick,skip)
            dp[i]=ans
            return ans
        return f(len(nums)-1)
        