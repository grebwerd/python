class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
      
        S = S.upper()
        if K is None or K < 1 or len(S) <1:
            return S
        
        S = S.replace("-","")
        print(S)
        strLength = len(S)
        
        retval = ""
        modulo = strLength%K
      
        counter = 0
        
        while( counter < strLength):
            if counter is 0 and modulo != 0:
                retval += S[counter:modulo]
                counter += modulo
            else:
                retval += S[counter:counter+K]
                counter += K
            
            
            if counter < strLength:
                retval += "-"
            
        
        
        return retval
            
        