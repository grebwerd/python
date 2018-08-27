import sys 

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = 0
        maxSoFar = -sys.maxsize-1

        for n in nums:
            m = max(m+n, n)
            maxSoFar = max(m, maxSoFar)
        return maxSoFar
