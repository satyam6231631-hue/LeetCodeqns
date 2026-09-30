# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root,key):
            if root is None:
                return False
            if root.val==key:
                return True
            elif root.val>key:
                return search(root.left,key)
            elif root.val<key:
                return search(root.right,key)
        def lca(root,p,q):
            if root.val>p and root.val>q:
                return lca(root.left,p,q)
            elif root.val<p and root.val<q:
                return lca(root.right,p,q)
            elif root.val==p or root.val==q:
                return root
            else:
                return root
            
        if search(root,p.val) and search(root,q.val):
            return lca(root,p.val,q.val)        