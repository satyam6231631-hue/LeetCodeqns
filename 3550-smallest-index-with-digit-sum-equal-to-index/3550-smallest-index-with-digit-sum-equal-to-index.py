class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
     
        def summ(n):
            s=0
            while(n>0):
                s+=(n%10)
                n=n//10
            return s

        for i in range(len(nums)):
            if summ(nums[i])==i:
                return i
        return -1
        