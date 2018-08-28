class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 1:
            return 1
        
        first = 1
        second = 2
        
        for n in range(3, n+1):
            temp = second + first
            first = second
            second = temp
            
        return second
            