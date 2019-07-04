class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n is None:
            return None
        
        retval = []
        
        for val in range(1,n+1):
            if val%3 == 0 and val%5 != 0:
                retval.append("Fizz")
            elif val%5 == 0 and val%3 != 0:
                retval.append("Buzz")
            elif val%3 == 0 and val%5 == 0:
                retval.append("FizzBuzz")
            else:
                retval.append(str(val))
            
        return retval
