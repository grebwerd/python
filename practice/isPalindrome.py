class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None or (x <10 and x >= 0):
            return True
        intAsStr = str(x)
        length = len(intAsStr)
        pivot = (length/2)-1
       
        for index, value in enumerate(intAsStr):
            if index > pivot:
                return True
            if intAsStr[index] != intAsStr[length-index-1]:
                return False        
