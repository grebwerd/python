class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax = 0
        currMax = 0
        for n in nums:
            temp = currMax
            # print("The currMax is", currMax)
            # print("The prevMax is ", prevMax, " and n is ", n, " prev+n is ", (prevMax+n))
            currMax = max(prevMax+n, currMax)
            prevMax = temp
        # print("the total is ", currMax)
        return currMax