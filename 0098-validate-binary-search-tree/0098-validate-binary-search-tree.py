# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst(self,root,low,high):
        if root is None:
            return True
        if root.val<low or root.val>high:
            return False
        left=self.bst(root.left,low,root.val-1)
        right=self.bst(root.right,root.val+1,high)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root,float('-inf'),float('inf'))

        