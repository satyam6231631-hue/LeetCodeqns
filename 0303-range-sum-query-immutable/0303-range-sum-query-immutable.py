class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
      

        

    def sumRange(self, left: int, right: int) -> int:
        self.sum=0
        

        for i in range(left,right+1):
            self.sum+=self.nums[i]
        return self.sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums1
# param_1 = obj.sumRange(left,right)