class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lengthA = len(a)
        lengthB = len(b)
        if  lengthA is 0 and lengthB > 0:
            return b
        
        if  lengthA > 0 and lengthB is 0:
            return a
        
        if  lengthA is 0 and lengthB is 0:
            return ""
        
        
        if lengthA > lengthB:
            b = self.prependZero(b, (lengthA-lengthB))
         
        
        if lengthA < lengthB:
            a = self.prependZero(a, (lengthB-lengthA))
           
            
        length = max(lengthA,lengthB)
        hasCarry = False
        retval = ""
        for i, e in enumerate(a):
            if a[length-i-1] is "0" and b[length-i-1] is "0" and hasCarry is False:
                retval = "0"+ retval
            elif a[length-i-1] is "0" and b[length-i-1] is "0" and hasCarry is True:
                retval = "1"+ retval
                hasCarry = False
            elif a[length-i-1] is "1" and b[length-i-1] is "0" and hasCarry is False:
                retval = "1"+retval
            elif a[length-i-1] is "1" and b[length-i-1] is "0" and hasCarry is True:
                retval = "0"+retval
            elif a[length-i-1] is "0" and b[length-i-1] is "1" and hasCarry is False:
                retval = "1"+retval
            elif a[length-i-1] is "0" and b[length-i-1] is "1" and hasCarry is True:
                retval = "0"+retval
            elif a[length-i-1] is "1" and b[length-i-1] is "1" and hasCarry is False:
                retval = "0"+retval
                hasCarry = True
            elif a[length-i-1] is "1" and b[length-i-1] is "1" and hasCarry is True:
                retval = "1"+retval
            
        if hasCarry is True:
            retval = "1"+retval
            
       
        return retval
    
    def prependZero(self, str, size):
        return ("0"*size) + str
       
            
        