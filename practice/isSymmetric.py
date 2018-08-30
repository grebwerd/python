# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left = []
        right = []
        self.leftFirst(root, left)
        self.rightFirst(root, right)
        
#         print("Left values are")
#         for v in left:
#             print("v: ", v)
            
#         print("right values are")
#         for v in right:
#             print("v: ", v)

        for i, v in enumerate(left):
            if left[i] != right[i]:
                return False
            
        return True


    def leftFirst(self, root, l):
        if root:
            # print("leftFirst: appending the value,", root.val)
            l.append(root.val)
            self.leftFirst(root.left,l)
            self.leftFirst(root.right,l)
        else:
            l.append(-1)
            
    def rightFirst(self, root, l):
        if root:
            # print("rightFirst: appending the value,", root.val)
            l.append(root.val)
            self.rightFirst(root.right,l)
            self.rightFirst(root.left, l)
        else:
            l.append(-1)