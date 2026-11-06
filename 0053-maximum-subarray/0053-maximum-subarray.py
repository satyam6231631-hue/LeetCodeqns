class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ms=float('-inf')
        cs=0
        for i in range(len(nums)):
            cs+=nums[i]
            ms=max(cs,ms)
            if cs<0:
                cs=0
        return ms
        