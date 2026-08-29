# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def SumBST(root,low,high):
            if root is None:
                return 0
            elif low<=root.val<=high:
                return root.val+SumBST(root.left,low,high)+SumBST(root.right,low,high)
            elif root.val<low:
                return SumBST(root.right,low,high)
            else:
                return SumBST(root.left,low,high)
        return SumBST(root,low,high)

        