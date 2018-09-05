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
        if root is not None:
            print("The root value is", root.val, "p's value is", p.val, "q's value is", q.val)
        else:
            print("The root is None")
        
        #basecase if root is None or root is equal to p or root is equal to q then return root.
        if root is None or root is p or root is q:
            return root
        
        #traverse the tree recursively going left first
        left = self.lowestCommonAncestor(root.left, p, q)
        if left is not None:
            print("Left's value is", left.val)
        else:
            print("Left's value is None")
        
        
        #traverse the tree recursively going right second
        right = self.lowestCommonAncestor(root.right, p,q)
        if right is not None:
            print("Right's value is", right.val)
        else:
            print("Right's value is None")
        
        
        
        if left is None:
            if right is not None:
                print("Returning right values", right.val)
            else:
                print("Return right which is none")
            return right
        elif right is None:
            if left is not None:
                print("Returning left values", left.val)
            else:
                print("Return left which is none")
            return left
        else:
            if root is not None:
                print("Returning root values", root.val)
            else:
                print("Return root which is none") 
            return root