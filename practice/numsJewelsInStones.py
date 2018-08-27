class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        retval = 0

        for index, value in enumerate(S):
            if value in J:
                retval +=1
            
        return retval