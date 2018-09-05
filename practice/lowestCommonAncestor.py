# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        #basecase if root is None or root is equal to p or root is equal to q then return root.
        if root is None or root is p or root is q:
            return root
        
        #traverse the tree recursively going left first
        left = self.lowestCommonAncestor(root.left, p, q)

        #traverse the tree recursively going right second
        right = self.lowestCommonAncestor(root.right, p,q)
       
        
        
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root