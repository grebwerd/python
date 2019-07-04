class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) is 0:
            return ""
        
        retval = ""

        if len(strs) is 1:
            return strs[0]
        
        prefixWord = strs[0]
        
        if prefixWord == "":
             return ""

        for index, value in enumerate(prefixWord):
         
            for word in strs:
                if word.startswith(retval+value) is False:
                    return retval
            retval = retval + value
                
                    
        return retval

