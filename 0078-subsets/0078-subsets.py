class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,curr=[],[]
        def ss(idx):
            if idx==len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[idx])
            ss(idx+1)
            curr.pop()
            ss(idx+1)
        ss(0)
        return ans
            
                
        
        