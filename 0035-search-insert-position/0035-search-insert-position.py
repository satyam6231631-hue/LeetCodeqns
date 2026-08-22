class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start,end,ans=0,len(nums)-1,-1
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]<target:
                start=mid+1
                ans=mid
            else:
                end=mid-1
        return ans+1



        