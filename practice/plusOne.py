class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits.reverse()
        for index, value in enumerate(digits):
            if index is 0:
                temp  = value + 1
            else:
                temp = value + carry
            
            if temp >= 10:
                carry = 1
                digits[index] = temp % 10
                if index is len(digits)-1:
                    digits.append(0)
            else:
                digits[index] = temp
                carry = 0
        digits.reverse()
        return digits
        