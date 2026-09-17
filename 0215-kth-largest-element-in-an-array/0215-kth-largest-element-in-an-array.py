import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        for i in range(k):
            ans=-heapq.heappop(nums)
        return ans
      
        