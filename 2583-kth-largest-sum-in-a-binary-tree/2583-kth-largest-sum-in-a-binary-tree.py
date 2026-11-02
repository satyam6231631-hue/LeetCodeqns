# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        
        arr=[]
        q=deque([root])
        while q:
            s=0
            for _ in range(len(q)):
                node=q.popleft()
                s+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(arr,-s)
        if len(arr)<k:
            return -1
        for _ in range(k-1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)


        





            

      

        


        