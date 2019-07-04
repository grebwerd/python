class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        retval = 0

        for index, value in enumerate(s):

            if map.get(value) > map.get(s[index-1]) and index > 0:
                retval += map.get(value) - (2*map.get(s[index-1]))
            else:
                retval += map.get(value)

        return retval