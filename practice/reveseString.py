class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        text = list(s)
        length = len(text)
        
        if length <= 1:
            return s
        
        pivot = (length/2) -1
        for index, value in enumerate(text):
            if index > pivot:
                return ''.join(text)
            text[index],text[length-index -1] = text[length-index -1],text[index]