class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        s=0
        mx=0
        while(i<j):
            s=nums[i]+nums[j]
            mx=max(mx,s)
            i+=1
            j-=1
        return mx



        