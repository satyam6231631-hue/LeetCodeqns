class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        vst=[False]*(n+2)
        for i in nums:
            if 0<i<=n+1:
                vst[i]=True
        for i in range(1,n+2):
            if not vst[i]:
                return i
        
      
        
        
        