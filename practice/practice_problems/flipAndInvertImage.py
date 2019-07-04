class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for l in A:
            l.reverse()
            for index, value in enumerate(l):
                
                if value is 0:
                    l[index] = 1
                else:
                    l[index] = 0
        return A
        