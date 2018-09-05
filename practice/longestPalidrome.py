class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return ""
        
        maxLength = 0
        retval = ""
        for index in range(len(s)):
            oddLengthPalindrome = self.expandAroundCenter(s, index, index)
            evenLengthPalindrome = self.expandAroundCenter(s, index, index + 1)
            
            oddLength =  len(oddLengthPalindrome)
            evenLength = len(evenLengthPalindrome)
            
            if oddLength > evenLength and oddLength > maxLength:
                maxLength = oddLength
                retval = oddLengthPalindrome
            elif evenLength > oddLength and evenLength > maxLength:
                maxLength = evenLength
                retval =  evenLengthPalindrome
            
        return retval




    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while(L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
        #return the length of the palindrome
        return s[L+1:R]