class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n_col = len(A)
        n_row = len(A[0])
        output = [[[]for a in range(n_col)] for b in range(n_row)]

        for i in range(n_col):
            for j in range(n_row):
                output[j][i] =A[i][j]
        return output
        
