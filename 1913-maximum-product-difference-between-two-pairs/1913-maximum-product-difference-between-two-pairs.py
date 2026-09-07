class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # def part(nums,lo,hi):
        #     pivot,pos=nums[hi],lo-1
        #     for i in range(lo,hi+1):
        #         if nums[i]<=pivot:
        #             pos+=1
        #             nums[i],nums[pos]=nums[pos],nums[i]
        #     return pos
        # def qs(nums,lo,hi):
        #     if lo>=hi:
        #         return
        #     idx=part(nums,lo,hi)
        #     qs(nums,lo,idx-1)
        #     qs(nums,idx+1,hi)
        # qs(nums,0,len(nums)-1)
        nums.sort()
        return (nums[-1]*nums[-2])-(nums[0]*nums[1])
        