class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)/2
        retval = 0
        counter = 0
        startIndex = 0
        while counter < n:
            retval += nums[startIndex]
            startIndex +=2
            counter += 1
            
        return retval
            