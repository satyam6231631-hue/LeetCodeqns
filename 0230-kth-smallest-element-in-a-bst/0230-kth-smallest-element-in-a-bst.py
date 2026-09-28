# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        ct=0
        def ctt(root):
            nonlocal ct
            if root is None:
                return
            ans=ctt(root.left)
            if ans is not None:
                return ans
            ct+=1
            if ct==k:
                return root.val
            ans=ctt(root.right)
            if ans is not None:
                return ans
        return ctt(root)