class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        
        def dfs(root, path):
            if root is None:
                return []
            if root.left is None and root.right is None:
                path = path + [root.val]
                paths.append("->".join(map(str,path)))
                return
            path = path + [root.val]
            dfs(root.left, path)
            dfs(root.right, path)
        
        
        dfs(root, paths)

        return paths
        