class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans,curr=[],[]
        visit=[False]*(n)
        def pp(idx):
            if idx==len(nums):
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if visit[i]:
                    continue
                curr.append(nums[i])
                visit[i]=True
                pp(idx+1)
                curr.pop()
                visit[i]=False
        pp(0)
        return ans


            

        