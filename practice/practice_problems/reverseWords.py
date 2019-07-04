class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokens = s.split()
        retval = ""
        
        for token in tokens:
            retval =retval + " " + self.reverseWord(token)
        return retval[1:]
        
        
        
    def reverseWord(self, word):
        text = list(word)
        length = len(word)
        
        if length <= 1:
            return word
        
        pivot = (length/2) -1
        
        for index, value in enumerate(text):
            if( index > pivot):
                return "".join(text)
            
            text[index], text[length-index-1] = text[length-index-1],text[index]
        